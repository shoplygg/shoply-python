"""A stand-in for the API, for the tests: Python's own HTTP server in a thread, on a free port.
What it answers is decided by the X-Plan header a test sends; every request is kept in `seen`,
and a plan's count of tries in `tries`. Nothing here reaches Shoply."""

import email.parser
import email.policy
import json
import secrets
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, List, Optional

STORE = "11111111-2222-3333-4444-555555555555"


class StandIn:
    def __init__(self) -> None:
        self.seen: List[Dict[str, Any]] = []
        self.tries: Dict[str, int] = {}
        self.lock = threading.Lock()
        stand_in = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args: Any) -> None:
                pass

            def do_GET(self) -> None:
                stand_in.answer(self)

            do_POST = do_PUT = do_PATCH = do_DELETE = do_GET

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.server.daemon_threads = True
        self.base = f"http://127.0.0.1:{self.server.server_address[1]}/v1"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.server.shutdown()
        self.server.server_close()

    def fresh(self) -> None:
        with self.lock:
            self.seen.clear()
            self.tries.clear()

    def answer(self, handler: BaseHTTPRequestHandler) -> None:
        parts = urllib.parse.urlsplit(handler.path)
        path = parts.path
        query = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
        headers = {name.lower(): value for name, value in handler.headers.items()}
        length = int(headers.get("content-length") or 0)
        raw = handler.rfile.read(length) if length else b""
        plan = headers.get("x-plan", "")

        with self.lock:
            self.seen.append({
                "method": handler.command,
                "path": path,
                "query": query,
                "raw_query": parts.query,
                "body": raw.decode("utf-8", "replace"),
                "files": _files(headers.get("content-type", ""), raw),
                "headers": headers,
            })
            self.tries[plan] = self.tries.get(plan, 0) + 1
            tries = self.tries[plan]

        def send(status: int, data: Any, extra: Optional[Dict[str, Any]] = None, more: Optional[Dict[str, str]] = None) -> None:
            extra = dict(extra or {})
            body = {
                "success": status < 400,
                "message": None if status < 400 else extra.pop("message", "No."),
                "code": extra.pop("code", None),
                "data": data,
            }
            body.update(extra)
            text = json.dumps(body).encode("utf-8")
            handler.send_response(status)
            handler.send_header("Content-Type", "application/json")
            handler.send_header("Content-Length", str(len(text)))
            handler.send_header("X-Request-Id", "req-" + secrets.token_hex(3))
            for name, value in (more or {}).items():
                handler.send_header(name, value)
            handler.end_headers()
            handler.wfile.write(text)

        if path == "/v1/key":
            return send(200, {"store": {"id": STORE}})

        if plan == "503x2":
            return send(503, None, {"message": "Down."}) if tries <= 2 else send(200, {"id": "c1"})
        if plan == "500x1":
            return send(500, None) if tries <= 1 else send(200, {"id": "o1"})
        if plan == "429-1":
            return send(429, None, {"code": "rate_limited", "message": "Slow down."}, {"Retry-After": "1"}) if tries <= 1 else send(200, [])
        if plan == "429-120":
            return send(429, None, {"code": "rate_limited", "message": "Slow down."}, {"Retry-After": "120"})
        if plan == "409x1":
            return send(409, None, {"code": "request_in_progress"}) if tries <= 1 else send(200, {"id": "c1"})
        if plan == "422":
            return send(422, None, {"code": "validation_failed", "message": "Check the fields.", "errors": {"code": "Taken."}})
        if plan == "503":
            return send(503, None)
        if plan == "drop1" and tries <= 1:
            # Hung up on before a word of an answer: nothing was answered.
            handler.close_connection = True
            return None
        if plan == "redirect":
            handler.send_response(302)
            handler.send_header("Location", "/v1/elsewhere")
            handler.send_header("Content-Length", "0")
            handler.end_headers()
            return None
        if plan == "slow":
            time.sleep(1.5)
            return send(200, [])
        if plan == "csv":
            text = "﻿Order ID,Email\no1,a@example.com\n".encode("utf-8")
            handler.send_response(200)
            handler.send_header("Content-Type", "text/csv; charset=utf-8")
            handler.send_header("Content-Length", str(len(text)))
            handler.end_headers()
            handler.wfile.write(text)
            return None
        if plan == "pages":
            rows = [{"id": "o1"}, {"id": "o2"}, {"id": "o3"}, {"id": "o4"}, {"id": "o5"}]
            page = int(query.get("page", "1"))
            return send(200, rows[(page - 1) * 2:page * 2], {"pages": 3, "total": 5, "meta": {"statusCounts": {"all": 5}}})

        if path.endswith("/customer/login"):
            return send(200, {"sent": True})
        if path.endswith("/customer/verify"):
            return send(200, {"token": "shoply_ct_abc", "tokenType": "Bearer", "expiresAt": "2026-11-20T00:00:00Z", "email": "a@example.com"})
        if path.endswith("/customer/logout"):
            return send(200, None)
        if path.endswith("/customer/affiliate/join"):
            return send(500, None)

        return send(200, {"id": "o1", "email": "a@example.com"})


def _files(content_type: str, raw: bytes) -> Dict[str, Dict[str, Any]]:
    """The files of a multipart body, by field: their name, type and bytes."""
    if not content_type.startswith("multipart/form-data"):
        return {}

    message = email.parser.BytesParser(policy=email.policy.HTTP).parsebytes(b"Content-Type: " + content_type.encode() + b"\r\n\r\n" + raw)
    out = {}

    for part in message.iter_parts():
        field = part.get_param("name", header="content-disposition")
        out[str(field)] = {"name": part.get_filename(), "type": part.get_content_type(), "bytes": part.get_payload(decode=True)}

    return out
