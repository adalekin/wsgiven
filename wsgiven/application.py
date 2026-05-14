import functools
import re
from typing import ClassVar

from .middlewares import handle_error


class Application:
    default_middlewares: ClassVar[tuple] = (handle_error,)

    def __init__(self, routes, middlewares=None, config=None):
        self.data = {"config": config or {}}
        self.routes = [(re.compile("(?:" + route + r")\Z"), route_handler) for route, route_handler in routes.items()]
        self.middlewares = list(self.default_middlewares) + (middlewares or [])

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    @staticmethod
    def not_found(_application, _environ, start_fn):
        start_fn("404 Not Found", [("Content-Type", "text/plain")])
        return [b"404 Not Found"]

    def __call__(self, environ, start_fn):
        path = environ.get("PATH_INFO", "")
        handler = self.not_found

        for route, route_handler in self.routes:
            match = route.match(path)

            if match:
                handler = functools.partial(route_handler, **match.groupdict())

        handler = functools.reduce(lambda h, m: m(h), self.middlewares, handler)
        return handler(application=self, environ=environ, start_fn=start_fn)
