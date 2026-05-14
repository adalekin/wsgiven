"""Pytest fixtures for WSGI integration tests."""

import pytest
from werkzeug.test import Client

from wsgiven import Application


@pytest.fixture
def fx_application():
    """Empty application with no routes."""
    return Application(routes={})


@pytest.fixture
def fx_http_client(fx_application):
    """HTTP-style client that drives the WSGI app in-process (no real socket)."""
    return Client(fx_application)
