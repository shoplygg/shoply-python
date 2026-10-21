"""The Python SDK against a stand-in for the API (tests/standin.py, on a free port): what it
sends, what it does with each kind of answer, and webhooks. Nothing here reaches Shoply.

    python3 -m unittest discover -s tests
"""

import base64
import hashlib
import hmac
import json
import os
import re
import sys
import tempfile
import time
import unittest
import urllib.parse
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import shoply  # noqa: E402
from shoply import Client, Customer, File, Page, ShoplyError, oauth, webhooks  # noqa: E402
from shoply._generated.routes import ROUTES  # noqa: E402
from standin import STORE, StandIn  # noqa: E402

KEY = "shoply_sk_test0000000000000000000000000000000000000000"
PACKAGE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

stand_in: StandIn


def setUpModule() -> None:
    global stand_in
    stand_in = StandIn()


def tearDownModule() -> None:
    stand_in.stop()


def plan(name: str) -> dict:
    return {"headers": {"X-Plan": name}}


class Case(unittest.TestCase):
    def setUp(self) -> None:
        stand_in.fresh()
        self.client = Client(KEY, store_id=STORE, base_url=stand_in.base)

    @property
    def seen(self) -> list:
        return list(stand_in.seen)


class ThePackage(unittest.TestCase):
    def test_its_name_and_python(self) -> None:
        with open(os.path.join(PACKAGE, "pyproject.toml")) as handle:
            text = handle.read()
        self.assertIn('name = "shoply"', text)
        self.assertIn('requires-python = ">=3.9"', text)
        self.assertIn(f'version = "{shoply.VERSION}"', text)

    def test_every_route_is_a_method(self) -> None:
        client = Client(KEY, store_id=STORE)
        buyer = Customer(STORE)
        missing = []

        for id, route in ROUTES.items():
            owner: Any = buyer if route["customer"] else client
            parts = (re.sub(r"^customer\.", "", id) if route["customer"] else id).split(".")
            name = parts.pop()
            for part in parts:
                owner = getattr(owner, part + "_" if part in ("import", "class") else part, None)
            if not callable(getattr(owner, name + "_" if name in ("import", "class") else name, None)):
                missing.append(id)

        self.assertEqual(missing, [], f"every route of the reference is a method ({len(ROUTES)})")

    def test_a_keyword_takes_an_underscore(self) -> None:
        self.assertTrue(callable(Client(KEY, store_id=STORE).storefronts.import_))


class AKeyAndTheStore(Case):
    def test_no_key_is_refused(self) -> None:
        saved = os.environ.pop("SHOPLY_API_KEY", None)
        try:
            with self.assertRaises(ShoplyError) as caught:
                Client()
            self.assertEqual(caught.exception.code, "api_key_required")
            with self.assertRaises(ShoplyError):
                Client("shoply_ct_buyer")
            os.environ["SHOPLY_API_KEY"] = KEY
            Client()
        finally:
            os.environ.pop("SHOPLY_API_KEY", None)
            if saved is not None:
                os.environ["SHOPLY_API_KEY"] = saved

    def test_the_store_is_asked_of_the_key_once(self) -> None:
        client = Client(KEY, base_url=stand_in.base)
        client.orders.show("o1")
        client.orders.show("o2")
        seen = self.seen
        self.assertEqual([r["path"] for r in seen].count("/v1/key"), 1)
        self.assertEqual(seen[1]["path"], f"/v1/stores/{STORE}/orders/o1")
        self.assertEqual(seen[1]["headers"]["authorization"], "Bearer " + KEY)
        self.assertTrue(seen[1]["headers"]["user-agent"].startswith(f"shoply-python/{shoply.VERSION} (python/"))
        self.assertEqual(client.store_id(), STORE)

    def test_a_store_given_is_not_asked_for(self) -> None:
        self.client.orders.show("a/b c")
        self.assertEqual(len(self.seen), 1)
        self.assertEqual(self.seen[0]["path"], f"/v1/stores/{STORE}/orders/a%2Fb%20c")

    def test_an_empty_id_is_refused_before_anything_is_sent(self) -> None:
        with self.assertRaises(ValueError):
            self.client.orders.show("")
        self.assertEqual(self.seen, [])


class WhatGoesWhere(Case):
    def test_a_reads_fields_go_in_the_address(self) -> None:
        self.client.customers.list(search="ana", perPage=5)
        self.assertEqual(self.seen[0]["query"], {"page": "1", "search": "ana", "perPage": "5"})

    def test_a_changes_go_in_its_body(self) -> None:
        self.client.coupons.create(code="SAVE10", value=10, tz="Europe/Riga")
        request = self.seen[0]
        self.assertEqual(json.loads(request["body"]), {"code": "SAVE10", "value": 10})
        self.assertEqual(request["headers"]["content-type"], "application/json")
        self.assertEqual(request["query"], {"tz": "Europe/Riga"})

    def test_a_keyword_field_is_sent_by_its_name(self) -> None:
        self.client.orders.list(from_="2026-10-01", to="2026-10-21")
        self.assertEqual(self.seen[0]["query"].get("from"), "2026-10-01")

    def test_true_and_false_in_the_address(self) -> None:
        self.client.request("GET", "/stores/{storeId}/orders", query={"a": True, "b": False, "c": [1, 2]})
        self.assertEqual(self.seen[0]["raw_query"], "a=true&b=false&c=1&c=2")

    def test_a_change_with_no_fields_sends_an_empty_object(self) -> None:
        self.client.orders.markPaid("o1")
        self.assertEqual(self.seen[0]["body"], "{}")

    def test_a_field_set_to_none_is_left_out(self) -> None:
        self.client.coupons.create(code="SAVE10", value=10, maxUses=None)
        self.assertNotIn("maxUses", json.loads(self.seen[0]["body"]))


class TheKeyOnEveryTry(Case):
    def test_a_change_the_server_could_not_answer_is_tried_again(self) -> None:
        coupon = self.client.coupons.create(code="SAVE10", value=10, **plan("503x2"))
        keys = [r["headers"].get("idempotency-key") for r in self.seen]
        self.assertEqual(coupon, {"id": "c1"})
        self.assertEqual(len(self.seen), 3)
        self.assertRegex(keys[0] or "", r"^[0-9a-f-]{36}$")
        self.assertEqual(len(set(keys)), 1, "the same key on every try")

    def test_a_key_given_is_the_one_sent(self) -> None:
        self.client.coupons.create(code="SAVE20", value=20, idempotency_key="mine-1")
        self.client.orders.show("o1")
        self.assertEqual(self.seen[0]["headers"]["idempotency-key"], "mine-1")
        self.assertNotIn("idempotency-key", self.seen[1]["headers"], "a read carries none")

    def test_a_read_is_tried_again(self) -> None:
        order = self.client.orders.show("o1", **plan("500x1"))
        self.assertEqual(order["id"], "o1")
        self.assertEqual(len(self.seen), 2)

    def test_told_to_slow_down_it_waits_as_long_as_it_is_told(self) -> None:
        began = time.monotonic()
        self.client.orders.show("o1", **plan("429-1"))
        self.assertGreaterEqual(time.monotonic() - began, 0.9)
        self.assertEqual(len(self.seen), 2)

    def test_told_to_wait_more_than_a_minute_it_does_not(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            self.client.orders.show("o1", **plan("429-120"))
        self.assertEqual((caught.exception.status, caught.exception.retry_after), (429, 120))
        self.assertEqual(len(self.seen), 1)

    def test_the_same_request_still_running_is_waited_for(self) -> None:
        self.client.coupons.create(code="A1", value=1, **plan("409x1"))
        self.assertEqual(len(self.seen), 2)

    def test_a_refusal_is_not_tried_again(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            self.client.coupons.create(code="A1", value=1, **plan("422"))
        error = caught.exception
        self.assertEqual(len(self.seen), 1)
        self.assertEqual((error.status, error.code, error.message, error.errors), (422, "validation_failed", "Check the fields.", {"code": "Taken."}))
        self.assertEqual(str(error), "Check the fields.")
        self.assertTrue((error.request_id or "").startswith("req-"))

    def test_max_retries_0_tries_once(self) -> None:
        with self.assertRaises(ShoplyError):
            self.client.orders.show("o1", max_retries=0, **plan("503"))
        self.assertEqual(len(self.seen), 1)

    def test_a_change_with_no_key_is_never_sent_again(self) -> None:
        picture = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        picture.write(b"PNG")
        picture.close()
        try:
            with self.assertRaises(ShoplyError):
                self.client.productImages.upload("p1", file=picture.name, **plan("503"))
            self.assertEqual(len(self.seen), 1)
            self.assertNotIn("idempotency-key", self.seen[0]["headers"])
        finally:
            os.unlink(picture.name)


class NothingAnswering(Case):
    def test_nothing_answering_is_connection_error(self) -> None:
        nowhere = Client(KEY, store_id=STORE, base_url="http://127.0.0.1:9/v1", max_retries=1)
        with self.assertRaises(ShoplyError) as caught:
            nowhere.orders.show("o1")
        self.assertEqual((caught.exception.status, caught.exception.code), (0, "connection_error"))

    def test_a_read_nothing_answered_is_tried_again(self) -> None:
        order = self.client.orders.show("o1", **plan("drop1"))
        self.assertEqual(order["id"], "o1")
        self.assertEqual(len(self.seen), 2)

    def test_a_change_with_no_key_nothing_answered_is_not(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            self.client.productImages.upload("p1", file=b"PNG", filename="a.png", **plan("drop1"))
        self.assertEqual(caught.exception.code, "connection_error")
        self.assertEqual(len(self.seen), 1)

    def test_a_redirect_is_not_followed(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            self.client.orders.show("o1", **plan("redirect"))
        self.assertEqual(caught.exception.status, 302)
        self.assertEqual(len(self.seen), 1)

    def test_too_slow_is_timeout(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            self.client.orders.show("o1", timeout=0.3, max_retries=0, **plan("slow"))
        self.assertEqual(caught.exception.code, "timeout")


class Lists(Case):
    def test_a_list_is_a_page(self) -> None:
        first = self.client.orders.list(perPage=2, **plan("pages"))
        self.assertIsInstance(first, Page)
        self.assertEqual([row["id"] for row in first.data], ["o1", "o2"])
        self.assertEqual((first.page, first.pages, first.total), (1, 3, 5))
        self.assertEqual(first.meta, {"statusCounts": {"all": 5}})
        second = first.next_page()
        assert second is not None
        self.assertEqual([row["id"] for row in second.data], ["o3", "o4"])

    def test_a_for_loop_walks_every_row_of_every_page(self) -> None:
        self.assertEqual([row["id"] for row in self.client.orders.list(perPage=2, **plan("pages"))], ["o1", "o2", "o3", "o4", "o5"])
        self.assertEqual([row["id"] for row in self.client.orders.list(perPage=2, page=2, **plan("pages"))], ["o3", "o4", "o5"])

    def test_the_last_has_no_next(self) -> None:
        last = self.client.orders.list(perPage=2, page=3, **plan("pages"))
        self.assertFalse(last.has_next_page())
        self.assertIsNone(last.next_page())


class FilesAndUploads(Case):
    def test_a_file_is_a_file(self) -> None:
        file = self.client.orders.export(status="completed", **plan("csv"))
        self.assertIsInstance(file, File)
        self.assertTrue((file.content_type or "").startswith("text/csv"))
        self.assertTrue(file.body.startswith(b"\xef\xbb\xbf"), "its bytes, as they came")
        self.assertEqual(file.text(), "Order ID,Email\no1,a@example.com\n")

    def test_an_upload_is_sent_as_a_form(self) -> None:
        folder = tempfile.mkdtemp()
        path = os.path.join(folder, "cover.png")
        with open(path, "wb") as handle:
            handle.write(b"PNGBYTES")
        field = ROUTES["productImages.upload"]["upload"]

        try:
            self.client.productImages.upload("p1", file=path)
            self.client.productImages.upload("p1", file=b"RAW", filename="named.webp")
            with open(path, "rb") as opened:
                self.client.productImages.upload("p1", file=opened, content_type="image/x-test")
            files = [request["files"][field] for request in self.seen]
            self.assertEqual((files[0]["name"], files[0]["type"], files[0]["bytes"]), ("cover.png", "image/png", b"PNGBYTES"))
            self.assertEqual((files[1]["name"], files[1]["type"], files[1]["bytes"]), ("named.webp", "image/webp", b"RAW"))
            self.assertEqual((files[2]["name"], files[2]["type"]), ("cover.png", "image/x-test"))
            with self.assertRaises(ValueError):
                self.client.productImages.upload("p1", file=os.path.join(folder, "none.png"))

            stand_in.fresh()
            self.client.disputes.addFile("d1", file=path, kind="communication")
            self.assertEqual(self.seen[0]["query"], {"kind": "communication"}, "what the route takes beside the file goes in the address")
            self.assertIn("file", self.seen[0]["files"])
        finally:
            os.unlink(path)
            os.rmdir(folder)


class AnyRouteByItsAddress(Case):
    def test_request_fills_in_the_store_and_answers_the_envelope(self) -> None:
        answer = self.client.request("GET", "/stores/{storeId}/orders", query={"page": 1})
        self.client.request("post", "/stores/{storeId}/coupons", body={"code": "X1", "value": 1})
        self.assertEqual(self.seen[0]["path"], f"/v1/stores/{STORE}/orders")
        self.assertIs(answer["success"], True)
        self.assertIn("data", answer)
        self.assertEqual(self.seen[1]["method"], "POST")
        self.assertIn("idempotency-key", self.seen[1]["headers"])


class TheCustomerApi(unittest.TestCase):
    def setUp(self) -> None:
        stand_in.fresh()

    def test_a_store_id_is_needed(self) -> None:
        with self.assertRaises(ShoplyError):
            Customer("")

    def test_signing_in_and_out(self) -> None:
        buyer = Customer(STORE, base_url=stand_in.base)

        with self.assertRaises(ShoplyError) as caught:
            buyer.show()
        self.assertEqual(caught.exception.code, "customer_token_required")
        self.assertEqual(stand_in.seen, [], "nothing is asked before signing in")

        buyer.login(email="a@example.com")
        login = stand_in.seen[0]
        self.assertEqual(login["path"], f"/v1/stores/{STORE}/customer/login")
        self.assertNotIn("authorization", login["headers"])
        self.assertNotIn("idempotency-key", login["headers"])
        self.assertEqual(json.loads(login["body"]), {"email": "a@example.com"})

        signed = buyer.verify(email="a@example.com", code="123456")
        self.assertEqual(signed["token"], "shoply_ct_abc")
        self.assertEqual(buyer.token, "shoply_ct_abc")

        me = buyer.show()
        self.assertEqual(me["email"], "a@example.com")
        self.assertEqual(stand_in.seen[2]["headers"]["authorization"], "Bearer shoply_ct_abc")

        stand_in.fresh()
        with self.assertRaises(ShoplyError):
            buyer.affiliate.join()
        self.assertEqual(len(stand_in.seen), 1, "a buyer's change with no key is not sent again")

        buyer.logout()
        self.assertIsNone(buyer.token)

    def test_a_kept_token_signs_in_again(self) -> None:
        Customer(STORE, base_url=stand_in.base, token="shoply_ct_kept").show()
        self.assertEqual(stand_in.seen[0]["headers"]["authorization"], "Bearer shoply_ct_kept")


class Webhooks(unittest.TestCase):
    secret = "whsec_test_secret"
    body = json.dumps({"id": "e1", "event": "order.paid", "createdAt": "2026-10-21T10:00:00Z", "storeId": STORE, "data": {"id": "o1"}})

    def test_sign_is_what_shoply_sends(self) -> None:
        headers = webhooks.sign(self.body, self.secret)
        digest = hmac.new(self.secret.encode(), (headers["X-Shoply-Timestamp"] + "." + self.body).encode(), hashlib.sha256).hexdigest()
        self.assertEqual(headers["X-Shoply-Signature"], "v1=" + digest)

    def test_a_signed_event_checks_out(self) -> None:
        headers = webhooks.sign(self.body, self.secret)
        event = webhooks.verify(self.body, headers, self.secret)
        self.assertEqual((event["event"], event["data"]["id"]), ("order.paid", "o1"))
        self.assertEqual(webhooks.verify(self.body.encode(), headers, self.secret)["id"], "e1", "as bytes")
        environ = {"HTTP_X_SHOPLY_TIMESTAMP": headers["X-Shoply-Timestamp"], "HTTP_X_SHOPLY_SIGNATURE": headers["X-Shoply-Signature"]}
        self.assertEqual(webhooks.verify(self.body, environ, self.secret)["id"], "e1", "a WSGI environ")
        lists = {"x-shoply-timestamp": [headers["X-Shoply-Timestamp"]], "x-shoply-signature": [headers["X-Shoply-Signature"]]}
        self.assertEqual(webhooks.verify(self.body, lists, self.secret)["id"], "e1", "lists")

    def test_what_is_refused(self) -> None:
        headers = webhooks.sign(self.body, self.secret)

        for payload, given, secret in ((self.body.replace("o1", "o2"), headers, self.secret), (self.body, headers, "another"), (self.body, {}, self.secret)):
            with self.assertRaises(ShoplyError) as caught:
                webhooks.verify(payload, given, secret)
            self.assertEqual(caught.exception.code, "invalid_signature")

        old = webhooks.sign(self.body, self.secret, int(time.time()) - 600)
        with self.assertRaises(ShoplyError) as caught:
            webhooks.verify(self.body, old, self.secret)
        self.assertEqual(caught.exception.code, "too_old")
        self.assertEqual(webhooks.verify(self.body, old, self.secret, tolerance=900)["id"], "e1")


class OAuth(Case):
    def test_an_apps_token_is_a_key_too(self) -> None:
        Client("shoply_at_" + "a" * 48, store_id=STORE, base_url=stand_in.base).orders.list()
        self.assertEqual(self.seen[-1]["headers"]["authorization"], "Bearer shoply_at_" + "a" * 48)

    def test_the_address_to_send_a_seller_to(self) -> None:
        url = oauth.authorize_url("shoply_app_0123456789abcdef", "https://app.example/back", state="s1", code_challenge="c" * 43)
        parts = urllib.parse.urlsplit(url)
        self.assertEqual(f"{parts.scheme}://{parts.netloc}{parts.path}", "https://dashboard.shoply.gg/oauth/authorize/")
        self.assertEqual(dict(urllib.parse.parse_qsl(parts.query)), {
            "response_type": "code",
            "client_id": "shoply_app_0123456789abcdef",
            "redirect_uri": "https://app.example/back",
            "state": "s1",
            "code_challenge": "c" * 43,
            "code_challenge_method": "S256",
        })
        self.assertNotIn("code_challenge", oauth.authorize_url("x", "https://a.example"))
        with self.assertRaises(ValueError):
            oauth.authorize_url("x", "")

    def test_a_pkce_pair_and_a_state(self) -> None:
        pair = oauth.pkce()
        self.assertRegex(pair["verifier"], r"^[A-Za-z0-9_-]{43}$")
        expected = base64.urlsafe_b64encode(hashlib.sha256(pair["verifier"].encode()).digest()).decode().rstrip("=")
        self.assertEqual(pair["challenge"], expected)
        self.assertEqual(pair["method"], "S256")
        self.assertNotEqual(oauth.state(), oauth.state())

    def test_a_code_swapped_with_the_secret(self) -> None:
        token = oauth.exchange(client_id="shoply_app_0123456789abcdef", client_secret="shoply_cs_secret", code="good", redirect_uri="https://app.example/back", base_url=stand_in.base)
        sent = self.seen[-1]
        form = dict(urllib.parse.parse_qsl(sent["body"]))
        self.assertEqual(token, {"access_token": "shoply_at_" + "b" * 48, "token_type": "Bearer", "scopes": ["orders.read", "products.read"], "store_id": STORE})
        self.assertEqual(sent["path"], "/v1/oauth/token")
        self.assertEqual(sent["headers"]["content-type"], "application/x-www-form-urlencoded")
        self.assertEqual(sent["headers"]["authorization"], "Basic " + base64.b64encode(b"shoply_app_0123456789abcdef:shoply_cs_secret").decode())
        self.assertEqual(form["grant_type"], "authorization_code")
        self.assertNotIn("client_id", form)

    def test_a_desktop_app_sends_the_verifier_and_no_secret(self) -> None:
        oauth.exchange(client_id="shoply_app_0123456789abcdef", code="good", redirect_uri="http://127.0.0.1/cb", code_verifier="v" * 43, base_url=stand_in.base)
        sent = self.seen[-1]
        form = dict(urllib.parse.parse_qsl(sent["body"]))
        self.assertNotIn("authorization", sent["headers"])
        self.assertEqual(form["client_id"], "shoply_app_0123456789abcdef")
        self.assertEqual(form["code_verifier"], "v" * 43)

    def test_a_refusal_is_oauths_word(self) -> None:
        with self.assertRaises(ShoplyError) as caught:
            oauth.exchange(client_id="x", client_secret="y", code="bad", redirect_uri="https://a.example", base_url=stand_in.base)
        self.assertEqual((caught.exception.status, caught.exception.code, caught.exception.message), (400, "invalid_grant", "The code is not right."))

    def test_a_token_given_up(self) -> None:
        oauth.revoke(client_id="shoply_app_0123456789abcdef", client_secret="shoply_cs_secret", token="shoply_at_x", base_url=stand_in.base)
        self.assertEqual(self.seen[-1]["path"], "/v1/oauth/revoke")
        self.assertEqual(dict(urllib.parse.parse_qsl(self.seen[-1]["body"]))["token"], "shoply_at_x")


if __name__ == "__main__":
    unittest.main()
