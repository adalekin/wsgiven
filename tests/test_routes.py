import pytest

from wsgiven import Application
from wsgiven.middlewares import handle_error
from wsgiven.utils.wsgi import jsonify


def _test_handler(application, environ, start_fn):  # noqa pylint: disable=unused-argument
    status = "200 OK"
    response_body, headers = jsonify({})
    return status, response_body, headers


def _test_handler_with_parameters(application, environ, start_fn, *args, **kwargs):  # noqa pylint: disable=unused-argument
    status = "200 OK"
    response_body, headers = jsonify(kwargs)
    return status, response_body, headers


@pytest.mark.parametrize("path", ["/test", "/test/test"])
def test_routes_simple(path):
    application = Application(routes={path: _test_handler}, middlewares=[handle_error])
    response = application(environ={"PATH_INFO": path}, start_fn=lambda status, headers: None,)

    assert response[0] == "200 OK"


@pytest.mark.parametrize("path", ["/test", "/test/test"])
def test_routes_simple_not_found(path):
    application = Application(routes={path: _test_handler}, middlewares=[handle_error])
    response = application(environ={"PATH_INFO": path + "1"}, start_fn=lambda status, headers: None,)

    assert response[0] == b"404 Not Found"


@pytest.mark.parametrize("route,path", [(r"^/test/(?P<id>\d+)/?$", "/test/123")])
def test_routes_regex(route, path):
    application = Application(routes={route: _test_handler_with_parameters}, middlewares=[handle_error])
    response = application(environ={"PATH_INFO": path}, start_fn=lambda status, headers: None,)

    assert response[0] == "200 OK"
