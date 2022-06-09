from http.client import HTTPConnection
import unittest
import requests
from unittest.mock import Mock, patch
from ward import test

@test("Making sure that tests are running")
def _():
    assert 42 in [21, 42, 138]
    
    
@test("Todos can be retrieved")
def _():
    response = requests.get()

@test("Testing connection")
def _():
        response = requests.get('http://127.0.0.1:8000/todo/')
        assert(response.ok)


if __name__ == '__main__':
    unittest.main()

    