"""Shoply's API from your own server: every route as a method, safe retries, pages, and checking
webhooks. Docs: https://docs.shoply.gg/api-reference/python

    import shoply

    client = shoply.Client()  # SHOPLY_API_KEY from the environment
    order = client.orders.show("8f2c...")
"""

from . import _webhooks as webhooks
from ._client import Client
from ._customer import Customer
from ._errors import ShoplyError
from ._files import File
from ._generated.routes import EVENTS
from ._generated.types import WebhookEvent, WebhookEventName
from ._page import Page
from ._version import VERSION

__all__ = ["Client", "Customer", "ShoplyError", "File", "Page", "webhooks", "WebhookEvent", "WebhookEventName", "EVENTS", "VERSION"]
