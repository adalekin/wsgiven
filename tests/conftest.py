import pytest
from wsgiref_fake.http.client import HTTPClient
from wsgiref_fake.server import make_server

from wsgiven import Application


@pytest.fixture(scope="function")
def fx_application():
    return Application(routes={})


@pytest.fixture(scope="function")
def fx_server(fx_application):  # noqa pylint: disable=redefined-outer-name
    return make_server(app=fx_application)


@pytest.fixture(scope="function")
def fx_http_client(fx_server):  # noqa pylint: disable=redefined-outer-name
    return HTTPClient(server=fx_server)
