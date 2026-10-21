"""Checking that a webhook came from Shoply, and making a signed one to test your handler with."""

import hashlib
import hmac
import json
import time
from typing import Any, Dict, Iterable, Optional, Protocol, Tuple, Union, cast

from ._errors import ShoplyError
from ._generated.types import WebhookEvent


class Headers(Protocol):
    """A request's headers: a dict, Django's `request.headers`, Flask's (which is no Mapping), or
    a WSGI environ. Anything with `items()`."""

    def items(self) -> Iterable[Tuple[str, Any]]: ...


def verify(payload: Union[str, bytes], headers: Headers, secret: str, tolerance: int = 300) -> WebhookEvent:
    """The event, once its signature checks out with the endpoint's signing secret and it was sent
    within `tolerance` seconds. Pass the raw body, as it arrived (Flask's `request.get_data()`,
    Django's `request.body`), and the request's headers, or a WSGI environ. Raises a ShoplyError
    with code `invalid_signature` or `too_old` otherwise."""
    if not secret:
        raise ValueError("Pass the endpoint's signing secret, from its page under Developers, Webhooks.")

    text = payload.decode("utf-8") if isinstance(payload, (bytes, bytearray)) else payload

    if not isinstance(text, str):
        raise TypeError("Pass the request's raw body, as it arrived: a str or bytes. A parsed object can't be checked.")

    timestamp = _header(headers, "X-Shoply-Timestamp")
    given = _header(headers, "X-Shoply-Signature")

    if not timestamp or not timestamp.isdigit() or not given:
        raise ShoplyError("The request has no Shoply signature: X-Shoply-Timestamp and X-Shoply-Signature.", code="invalid_signature")

    expected = "v1=" + hmac.new(secret.encode("utf-8"), f"{timestamp}.{text}".encode("utf-8"), hashlib.sha256).hexdigest()

    if not any(hmac.compare_digest(expected, one.strip()) for one in given.split(",")):
        raise ShoplyError("The signature does not match. Check the signing secret, and that the body is the raw one.", code="invalid_signature")

    if abs(time.time() - int(timestamp)) > tolerance:
        raise ShoplyError(f"The webhook was signed more than {tolerance} seconds ago.", code="too_old")

    return cast(WebhookEvent, json.loads(text))


def sign(payload: Union[str, bytes], secret: str, timestamp: Optional[int] = None) -> Dict[str, str]:
    """The headers Shoply would send with this body: for testing your own handler."""
    text = payload.decode("utf-8") if isinstance(payload, (bytes, bytearray)) else payload
    stamp = str(int(time.time()) if timestamp is None else timestamp)

    return {
        "X-Shoply-Timestamp": stamp,
        "X-Shoply-Signature": "v1=" + hmac.new(secret.encode("utf-8"), f"{stamp}.{text}".encode("utf-8"), hashlib.sha256).hexdigest(),
    }


def _header(headers: Headers, name: str) -> Optional[str]:
    """A header by its name whatever its case, a list's first value, or as a WSGI environ names it."""
    environ = "HTTP_" + name.upper().replace("-", "_")

    for key, value in headers.items():
        if str(key).lower() == name.lower() or key == environ:
            value = value[0] if isinstance(value, (list, tuple)) else value
            return value if isinstance(value, str) else None

    return None
