"""Pytest fixtures for WSGI integration tests."""

import pytest
from werkzeug.test import Client

from wsgiven import Application


@pytest.fixture(scope="function")
def fx_application():
    """Empty application with no routes."""
    return Application(routes={})


@pytest.fixture(scope="function")
def fx_http_client(fx_application):  # pylint: disable=redefined-outer-name
    """HTTP-style client that drives the WSGI app in-process (no real socket)."""
    return Client(fx_application)
