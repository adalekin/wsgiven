# wsgiven

[![CI](https://github.com/adalekin/wsgiven/actions/workflows/ci.yml/badge.svg)](https://github.com/adalekin/wsgiven/actions/workflows/ci.yml)
[![PyPI publish](https://github.com/adalekin/wsgiven/actions/workflows/release.yml/badge.svg)](https://github.com/adalekin/wsgiven/actions/workflows/release.yml)
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
uv run ruff check wsgiven tests
uv run ruff format --check wsgiven tests
uv run pytest
```

To refresh dev dependencies and regenerate the lockfile:

```bash
uv lock --upgrade
```

To apply Ruff formatting (instead of only checking):

```bash
uv run ruff format wsgiven tests
```

## Contributing

Issues and **pull requests** (including from forks) are welcome. Please run `uv run ruff check`, `uv run ruff format --check`, and `uv run pytest` before submitting a change.

**Releases:** PyPI uploads are done only via this repository’s release workflow when a maintainer pushes a version tag. Forks and outside contributors cannot trigger that path for this repo. If you grant **write** access to collaborators, restrict the GitHub **pypi** [environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) with **required reviewers** so only you (or chosen maintainers) can approve a publish run.

## License

MIT — see [LICENSE](LICENSE).
