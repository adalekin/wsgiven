from .utils.log import LOG


def handle_error(handler):
    def _inner(application, environ, start_fn):
        try:
            return handler(application, environ, start_fn)
        except Exception:  # noqa: BLE001
            LOG.exception("Exception occurs")

            start_fn("500 Server Error", [("Content-Type", "text/plain")])
            return [b"500 Server Error"]

    return _inner
