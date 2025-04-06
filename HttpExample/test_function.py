import pytest
from HttpExample import main  # Assuming your function is in HttpExample/__init__.py or __main__.py

class DummyRequest:
    def __init__(self, method="GET"):
        self.method = method

    def get_json(self):
        return {}

    def params(self):
        return {}

def test_response_status_code():
    req = DummyRequest()
    resp = main(req)
    assert resp.status_code == 200

def test_response_content():
    req = DummyRequest()
    resp = main(req)
    assert resp.get_body().decode() == "Hello, World!"

def test_http_method():
    req = DummyRequest(method="GET")
    resp = main(req)
    assert req.method == "GET"
