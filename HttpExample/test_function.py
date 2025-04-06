import pytest
from . import __init__ as function
from unittest.mock import MagicMock

class DummyRequest:
    def __init__(self, method="GET"):
        self.method = method
    def get_json(self):
        return {}
    def params(self):
        return {}

def test_response_status_code():
    req = DummyRequest()
    resp = function.main(req)
    assert resp.status_code == 200

def test_response_content():
    req = DummyRequest()
    resp = function.main(req)
    assert resp.get_body().decode() == "Hello, World!"

def test_http_method():
    req = DummyRequest(method="GET")
    resp = function.main(req)
    assert req.method == "GET"

