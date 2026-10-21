"""Asking the API: one request, tried again where that is safe. Python's own urllib, nothing else."""

import json
import mimetypes
import os
import platform
import random
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Dict, Optional, Tuple, Union

from ._errors import ShoplyError
from ._files import File
from ._version import VERSION

API = "https://api.shoply.gg/v1"

# Statuses a request that is safe to repeat is tried again on.
AGAIN = {408, 429, 500, 502, 503, 504}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """A redirect is answered as it is: the API never sends one, and a key never follows one."""

    def redirect_request(self, *args: Any, **kwargs: Any) -> None:
        return None


_opener = urllib.request.build_opener(_NoRedirect)


class Transport:
    def __init__(self, base_url: Optional[str], timeout: float, max_retries: int, auth: Callable[[], Optional[str]]) -> None:
        self.base_url = (base_url or API).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.auth = auth

    def send(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Any = None,
        form: Optional[Tuple[str, Any, Optional[str], Optional[str]]] = None,
        idempotent: bool = False,
        file: bool = False,
        options: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], File]:
        """One request: `path` after /v1, `query` into the address, `body` as JSON or `form` as
        multipart. Answers the decoded envelope, or a File for a route that answers one."""
        options = options or {}
        url = self.base_url + path

        if query:
            pairs = []
            for name, value in query.items():
                if value is None:
                    continue
                for one in value if isinstance(value, (list, tuple)) else [value]:
                    pairs.append((name, "true" if one is True else "false" if one is False else str(one)))
            if pairs:
                url += "?" + urllib.parse.urlencode(pairs)

        headers = {"Accept": "application/json", "User-Agent": f"shoply-python/{VERSION} (python/{platform.python_version()})"}
        token = self.auth()

        if token:
            headers["Authorization"] = f"Bearer {token}"

        data: Optional[bytes] = None

        if form is not None:
            boundary = "shoply-" + uuid.uuid4().hex
            data = _multipart(boundary, *form)
            headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        elif body is not None:
            data = json.dumps(body, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"

        # A change carries a key of its own, the same on every try, so that a try whose answer was
        # lost is answered as the first was rather than carried out twice.
        key = (options.get("idempotency_key") or str(uuid.uuid4())) if idempotent else None

        if key:
            headers["Idempotency-Key"] = key

        headers.update(options.get("headers") or {})

        retries = self.max_retries if options.get("max_retries") is None else int(options["max_retries"])
        timeout = self.timeout if options.get("timeout") is None else float(options["timeout"])
        safe = method == "GET" or key is not None
        attempt = 0

        while True:
            request = urllib.request.Request(url, data=data, method=method, headers=headers)

            try:
                with _opener.open(request, timeout=timeout) as answer:
                    status = answer.status
                    answer_headers = {name.lower(): value for name, value in answer.headers.items()}
                    raw = answer.read()
            except urllib.error.HTTPError as error:
                status = error.code
                answer_headers = {name.lower(): value for name, value in (error.headers or {}).items()}
                raw = error.read() or b""
            except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as error:
                reason = getattr(error, "reason", error)
                timed_out = isinstance(reason, (socket.timeout, TimeoutError)) or isinstance(error, (socket.timeout, TimeoutError))
                failure = ShoplyError(
                    f"Shoply did not answer within {timeout:g} seconds." if timed_out else f"Shoply could not be reached: {reason}",
                    code="timeout" if timed_out else "connection_error",
                )

                # Whether a change that got no answer was made is not known: only one with a key
                # is sent again.
                if safe and attempt < retries:
                    time.sleep(_backoff(attempt))
                    attempt += 1
                    continue

                raise failure from error

            if 200 <= status < 300 and file:
                return File(raw, answer_headers)

            try:
                parsed = json.loads(raw.decode("utf-8")) if raw else None
            except ValueError:
                parsed = None

            if 200 <= status < 300 and isinstance(parsed, dict) and parsed.get("success") is not False:
                return parsed

            retry_after_text = answer_headers.get("retry-after", "")
            retry_after = int(retry_after_text) if retry_after_text.isdigit() else None
            code = parsed.get("code") if isinstance(parsed, dict) and isinstance(parsed.get("code"), str) else None
            message = parsed.get("message") if isinstance(parsed, dict) and parsed.get("message") else f"Shoply answered {status}."
            refusal = ShoplyError(
                str(message),
                status=status,
                code=code,
                errors=parsed.get("errors") if isinstance(parsed, dict) and isinstance(parsed.get("errors"), dict) else None,
                request_id=answer_headers.get("x-request-id"),
                retry_after=retry_after,
                body=parsed if parsed is not None else raw.decode("utf-8", "replace"),
            )

            # Told to slow down or to wait for the same request still running, and anything the
            # server could not answer: tried again, after as long as it said where it said, where
            # it is safe to. A change with no key is never sent again by itself.
            again = safe and attempt < retries and (status in AGAIN or (status == 409 and code == "request_in_progress"))

            if again and (retry_after is None or retry_after <= 60):
                time.sleep(retry_after if retry_after is not None else _backoff(attempt))
                attempt += 1
                continue

            raise refusal


def _backoff(attempt: int) -> float:
    """Half a second, then one, then two, up to eight, a little more or less."""
    return min(8.0, 0.5 * 2.0**attempt) * (0.75 + random.random() * 0.5)


def _multipart(boundary: str, field: str, file: Any, filename: Optional[str], content_type: Optional[str]) -> bytes:
    """One file as multipart/form-data, from a path, bytes or a file opened for reading."""
    if isinstance(file, (str, os.PathLike)):
        path = os.fspath(file)
        if not os.path.isfile(path):
            raise ValueError(f"There is no file at {path}.")
        with open(path, "rb") as handle:
            content = handle.read()
        filename = filename or os.path.basename(path)
    elif isinstance(file, (bytes, bytearray)):
        content = bytes(file)
    elif hasattr(file, "read"):
        content = file.read()
        filename = filename or os.path.basename(getattr(file, "name", "") or "") or None
    else:
        raise TypeError("An upload takes `file` as a path, bytes, or a file opened for reading.")

    filename = filename or "upload"
    content_type = content_type or mimetypes.guess_type(filename)[0] or "application/octet-stream"
    quoted = filename.replace('"', "%22")

    return (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"{field}\"; filename=\"{quoted}\"\r\nContent-Type: {content_type}\r\n\r\n".encode("utf-8")
        + content
        + f"\r\n--{boundary}--\r\n".encode("utf-8")
    )


