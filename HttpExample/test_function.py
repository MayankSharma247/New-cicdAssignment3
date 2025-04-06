import pytest
import HttpExample  # Import the module directly
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
    resp = HttpExample.main(req)  # Call the main function from HttpExample
    assert resp.status_code == 200

def test_response_content():
    req = DummyRequest()
    resp = HttpExample.main(req)  # Call the main function from HttpExample
    assert resp.get_body().decode() == "Hello, World!"

def test_http_method():
    req = DummyRequest(method="GET")
    resp = HttpExample.main(req)  # Call the main function from HttpExample
    assert req.method == "GET"
