from typing import Any, Dict, List, Optional

from ._calls import fill, prepare
from ._errors import ShoplyError
from ._generated.resources import CustomerResources
from ._transport import Transport


class Customer(CustomerResources):
    """The Customer API: a buyer signed in on your own site or app with a code emailed to them,
    reading their own orders, keys, subscriptions and affiliate page. It holds the buyer's token
    and no key.

        buyer = shoply.Customer(store_id="YOUR_STORE_ID")
        buyer.login(email=email)
        buyer.verify(email=email, code=code)  # keeps the token
        me = buyer.show()
    """

    def __init__(
        self,
        store_id: str,
        *,
        token: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 60.0,
        max_retries: int = 2,
    ) -> None:
        """
        store_id: the store's ID, from Settings, General. It is not a secret.
        token:    a token from an earlier sign-in (`shoply_ct_...`), if you kept one.
        """
        if not isinstance(store_id, str) or store_id == "":
            raise ShoplyError("Pass the store's ID as `store_id`. It is in Settings, General, in the store's dashboard.", code="store_id_required")

        self.store_id = store_id
        self.token = token
        self._transport = Transport(base_url, timeout, max_retries, lambda: self.token)
        self._resources()

    def _call(self, id: str, path: List[str], fields: Dict[str, Any], options: Dict[str, Any]) -> Any:
        route, values, query, body, _ = prepare(id, path, fields)

        if route["signed_in"] and not self.token:
            raise ShoplyError("Sign the buyer in first: login, then verify with the code they were emailed.", code="customer_token_required")

        answer = self._transport.send(
            route["method"], fill(route["path"], dict(values, storeId=self.store_id)),
            query=query, body=body, idempotent=False, options=options,
        )
        assert isinstance(answer, dict)
        data = answer.get("data")

        # Signing in hands out the token; signing out ends it.
        if id == "customer.verify" and isinstance(data, dict) and isinstance(data.get("token"), str):
            self.token = data["token"]

        if id in ("customer.logout", "customer.logoutEverywhere"):
            self.token = None

        return data
