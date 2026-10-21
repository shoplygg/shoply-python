import os
from typing import Any, Dict, List, Optional, Union

from ._calls import fill, prepare
from ._errors import ShoplyError
from ._files import File
from ._generated.resources import ClientResources
from ._page import Page
from ._transport import Transport


class Client(ClientResources):
    """Shoply's API from your own server, with a store's secret API key. Every route of the API
    reference is a method named by its id: `orders.show` is `client.orders.show(order_id)`.

        client = shoply.Client(api_key=os.environ["SHOPLY_API_KEY"])
        order = client.orders.show("8f2c...")

    A call takes the IDs in the route's address, in order, then its fields as keyword
    arguments, then options (`idempotency_key`, `timeout`, `max_retries`, `headers`). It answers
    the route's `data`, as dicts; a list that is paged answers a Page, and a file a File.

    Docs: https://docs.shoply.gg/api-reference/python
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        store_id: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 60.0,
        max_retries: int = 2,
    ) -> None:
        """
        api_key:     `shoply_sk_...`, or an app's token (`shoply_at_...`) from oauth.exchange(). Left
                     out, SHOPLY_API_KEY from the environment.
        store_id:    the store's ID. Left out, it is asked of the key the first time it is needed.
        timeout:     how long one try waits for an answer, in seconds. 60.
        max_retries: how many more tries a request that is safe to repeat is given. 2.
        """
        key = api_key if api_key is not None else os.environ.get("SHOPLY_API_KEY")

        if not isinstance(key, str) or not key.startswith(("shoply_sk_", "shoply_at_")):
            raise ShoplyError(
                "Pass the store's secret API key as `api_key` (shoply_sk_...), or an app's token (shoply_at_...), or set SHOPLY_API_KEY.",
                code="api_key_required",
            )

        self._store_id = store_id
        self._transport = Transport(base_url, timeout, max_retries, lambda: key)
        self._resources()

    def store_id(self) -> str:
        """The store the key belongs to, asked once and remembered."""
        if self._store_id is None:
            answer = self._transport.send("GET", "/key")
            assert isinstance(answer, dict)
            self._store_id = str(answer["data"]["store"]["id"])
        return self._store_id

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Any = None,
        idempotency_key: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Any route, by its method and its address after /v1, for one newer than this package:
        `{storeId}` in the path is filled in. Answers the whole envelope: `data`, and `meta`,
        `pages` and `total` where the route has them."""
        method = method.upper()
        if "{storeId}" in path:
            path = fill(path, {"storeId": self.store_id()})
        answer = self._transport.send(
            method, path, query=query, body=body, idempotent=method != "GET",
            options={"idempotency_key": idempotency_key, "timeout": timeout, "max_retries": max_retries, "headers": headers},
        )
        assert isinstance(answer, dict)
        return answer

    def _call(self, id: str, path: List[str], fields: Dict[str, Any], options: Dict[str, Any]) -> Any:
        route, values, query, body, form = prepare(id, path, fields)

        def fetch(page: int) -> Union[Dict[str, Any], File]:
            filled = dict(values)
            if "{storeId}" in route["path"]:
                filled["storeId"] = self.store_id()
            asked = dict(query or {}, page=page) if route["paged"] else query
            return self._transport.send(
                route["method"], fill(route["path"], filled), query=asked, body=body, form=form,
                idempotent=route["idempotent"], file=route["file"], options=options,
            )

        if route["paged"]:
            given = fields.get("page")
            return _page(fetch, given if isinstance(given, int) and given > 0 else 1)

        answer = fetch(1)
        return answer if isinstance(answer, File) else answer.get("data")


def _page(fetch: Any, number: int) -> Page[Any]:
    answer = fetch(number)
    data = answer.get("data")
    return Page(
        list(data) if isinstance(data, list) else [],
        number,
        int(answer["pages"]) if isinstance(answer.get("pages"), int) else None,
        int(answer["total"]) if isinstance(answer.get("total"), int) else None,
        answer.get("meta") if isinstance(answer.get("meta"), dict) else None,
        lambda next: _page(fetch, next),
    )
