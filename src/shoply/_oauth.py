"""Connecting an app to a seller's store, by OAuth's authorization code flow.

    1. Send the seller to authorize_url(). With PKCE (always, for a desktop or phone app), make a
       pair with pkce() first, keep its verifier and send its challenge.
    2. They come back to your redirect URL with `code` and your `state`. Check the state.
    3. exchange() the code, on your server with the client secret, or with the verifier.
    4. The token is a key of their store: shoply.Client(token). It works until the seller
       disconnects the app; revoke() gives it up.

Docs: https://docs.shoply.gg/guides/oauth
"""

import base64
import hashlib
import json
import platform
import secrets
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, TypedDict

from ._errors import ShoplyError
from ._version import VERSION

DASHBOARD = "https://dashboard.shoply.gg"
API = "https://api.shoply.gg/v1"


class Pkce(TypedDict):
    verifier: str
    challenge: str
    method: str


class Token(TypedDict):
    """A token of the seller's store, until they disconnect the app. Pass `access_token` as the key."""

    access_token: str
    token_type: str
    scopes: List[str]
    store_id: str


def _base64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def authorize_url(
    client_id: str,
    redirect_uri: str,
    *,
    state: Optional[str] = None,
    code_challenge: Optional[str] = None,
    dashboard_url: str = DASHBOARD,
) -> str:
    """The page to send a seller to. `state` is yours, sent back unchanged: check it."""
    if not client_id or not redirect_uri:
        raise ValueError("Pass the app's client_id and the redirect_uri the seller is sent back to.")

    query: Dict[str, str] = {"response_type": "code", "client_id": client_id, "redirect_uri": redirect_uri}

    if state:
        query["state"] = state

    if code_challenge:
        query["code_challenge"] = code_challenge
        query["code_challenge_method"] = "S256"

    return dashboard_url.rstrip("/") + "/oauth/authorize/?" + urllib.parse.urlencode(query, quote_via=urllib.parse.quote)


def pkce() -> Pkce:
    """A PKCE pair: keep `verifier` until the code comes back, and send `challenge`."""
    verifier = _base64url(secrets.token_bytes(32))

    return {"verifier": verifier, "challenge": _base64url(hashlib.sha256(verifier.encode("ascii")).digest()), "method": "S256"}


def state() -> str:
    """A random `state`, to keep with the seller's session and compare when they come back."""
    return _base64url(secrets.token_bytes(16))


def exchange(
    *,
    client_id: str,
    code: str,
    redirect_uri: str,
    client_secret: Optional[str] = None,
    code_verifier: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Token:
    """The code swapped for the token. A web app sends its client secret; a desktop or phone app
    sends the PKCE verifier and no secret. Raises a ShoplyError whose `code` is OAuth's word:
    `invalid_grant` (the code is wrong, used, or older than ten minutes), `invalid_client`."""
    if not client_id or not code or not redirect_uri:
        raise ValueError("Pass client_id, the code and the redirect_uri it came back to.")

    form = {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri}

    if code_verifier:
        form["code_verifier"] = code_verifier

    body = _post("/oauth/token", form, client_id, client_secret, base_url)

    return {
        "access_token": str(body.get("access_token", "")),
        "token_type": str(body.get("token_type", "")),
        "scopes": [one for one in str(body.get("scope", "")).split(" ") if one],
        "store_id": str(body.get("store_id", "")),
    }


def revoke(*, client_id: str, token: str, client_secret: Optional[str] = None, base_url: Optional[str] = None) -> None:
    """A token given up: it stops working at once. Answered the same whether or not there was one."""
    if not client_id or not token:
        raise ValueError("Pass client_id and the token to give up.")

    _post("/oauth/revoke", {"token": token}, client_id, client_secret, base_url)


def _post(path: str, form: Dict[str, str], client_id: str, client_secret: Optional[str], base_url: Optional[str]) -> Dict[str, Any]:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "User-Agent": f"shoply-python/{VERSION} (python/{platform.python_version()})",
    }

    if client_secret:
        pair = urllib.parse.quote(client_id, safe="") + ":" + urllib.parse.quote(client_secret, safe="")
        headers["Authorization"] = "Basic " + base64.b64encode(pair.encode("utf-8")).decode("ascii")
    else:
        form = {**form, "client_id": client_id}

    request = urllib.request.Request(
        (base_url or API).rstrip("/") + path,
        data=urllib.parse.urlencode(form).encode("ascii"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as answer:
            text = answer.read().decode("utf-8")
    except urllib.error.HTTPError as refused:
        text = refused.read().decode("utf-8", "replace")
        said: Dict[str, Any] = {}

        try:
            parsed = json.loads(text) if text else {}
            said = parsed if isinstance(parsed, dict) else {}
        except ValueError:
            said = {}

        retry = refused.headers.get("Retry-After") if refused.headers else None

        raise ShoplyError(
            str(said.get("error_description") or said.get("message") or f"Shoply answered {refused.code}."),
            status=refused.code,
            code=str(said.get("error") or ("rate_limited" if refused.code == 429 else "oauth_error")),
            retry_after=int(retry) if retry and retry.isdigit() else None,
            body=said or text,
        ) from None
    except (urllib.error.URLError, OSError) as failed:
        raise ShoplyError(f"Shoply could not be reached: {failed}", code="connection_error") from None

    parsed = json.loads(text) if text else {}

    return parsed if isinstance(parsed, dict) else {}
