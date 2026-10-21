# shoply

Shoply's API from your own server. Every route of the [API reference](https://docs.shoply.gg/api-reference/introduction) is a method, with types your editor and mypy read, safe retries, lists a page at a time or all at once, and checking that a webhook came from Shoply.

```sh
pip install shoply
```

Python 3.9 or later. No dependencies.

```python
import shoply

client = shoply.Client()  # SHOPLY_API_KEY from the environment

order = client.orders.show("ORDER_ID")

for customer in client.customers.list(search="gmail.com"):
    print(customer["emailAddress"])

coupon = client.coupons.create(code="SPRING10", value=10)
```

Make the key under **Developers**, **API Keys** in the dashboard, with the permissions your code needs. Keep it on your server.

A route's method is its id: **Get an order** is `orders.show`, so `client.orders.show(order_id)`. The address's IDs come first, in order, then the fields as keyword arguments, by the names the reference gives them, then options. A field whose name is a Python keyword takes an underscore: `from_`.

## Errors

A refusal is a `shoply.ShoplyError`, with `status`, `code` (`not_found`, `missing_scope`, `validation_failed`...), `errors` for each field that is wrong, and `request_id`.

```python
try:
    client.coupons.create(code="SPRING10", value=10)
except shoply.ShoplyError as error:
    if error.code == "validation_failed":
        print(error.errors)
```

A change is sent with an `Idempotency-Key`, the same on every try, so a try whose answer was lost is never carried out twice. Pass `idempotency_key=...` to use your own.

## Webhooks

```python
import os

import shoply
from flask import Flask, request

app = Flask(__name__)


@app.post("/webhooks/shoply")
def shoply_webhook() -> tuple[str, int]:
    try:
        event = shoply.webhooks.verify(request.get_data(), request.headers, os.environ["SHOPLY_WEBHOOK_SECRET"])
    except shoply.ShoplyError:
        return "", 401

    if event["event"] == "order.paid":
        ...  # event["data"] is the order

    return "", 200
```

## The Customer API

`shoply.Customer` signs a buyer in with a code emailed to them, and reads their own orders, keys and subscriptions. It holds the buyer's token and no key.

```python
buyer = shoply.Customer("YOUR_STORE_ID")

buyer.login(email=email)
buyer.verify(email=email, code=code)
me = buyer.show()
```

The whole guide: https://docs.shoply.gg/api-reference/python
