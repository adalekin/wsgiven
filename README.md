# wsgiven

[![CI](https://github.com/adalekin/wsgiven/actions/workflows/ci.yml/badge.svg)](https://github.com/adalekin/wsgiven/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**wsgiven** is a small WSGI toolkit: route `PATH_INFO` with regular expressions, stack middlewares, and optionally wrap handlers with shared utilities (for example JSON responses or centralized error handling).

The package has **no runtime dependencies** beyond the Python standard library.

## Requirements

- Python 3.10 or newer

## Install

From a clone of this repository:

```bash
uv pip install .
```

Or with pip:

```bash
pip install .
```

After the package is published on PyPI, `pip install wsgiven` will work as well.

## Quick example

```python
from wsgiven import Application
from wsgiven.middlewares import handle_error
from wsgiven.utils.wsgi import jsonify


def hello(application, environ, start_fn):
    status = "200 OK"
    body, headers = jsonify({"message": "hello"})
    return status, body, headers


app = Application(
    routes={r"^/$": hello},
    middlewares=[handle_error],
)
```

Use it with any WSGI server (for example Gunicorn, uWSGI, or `wsgiref.simple_server` for local runs).

## Development

Clone the repository, then install dev dependencies (uses the committed `uv.lock`) and run checks:

```bash
uv sync --locked
uv run pytest
uv run pylint wsgiven tests
```

To refresh dev dependencies and regenerate the lockfile:

```bash
uv lock --upgrade
```

## Contributing

Issues and pull requests are welcome. Please run `uv run pytest` and `uv run pylint wsgiven tests` before submitting a change.

## License

MIT — see [LICENSE](LICENSE).
