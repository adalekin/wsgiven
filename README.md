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

## Publishing to PyPI

Releases are automated: push a git tag whose name starts with `v` and matches the version in `wsgiven/__init__.py` (for example `v1.0.3` when `VERSION = "1.0.3"`).

1. **PyPI — Trusted Publisher**  
   In the PyPI project for `wsgiven`, add a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) for GitHub: set the repository owner/name, workflow file **`.github/workflows/release.yml`**, and environment **`pypi`**.

2. **GitHub — Environment**  
   In the repo: **Settings → Environments → New environment** → name **`pypi`**. You can leave protection rules empty or add required reviewers for production releases.

3. **Tag and push**

   ```bash
   git tag -a v1.0.3 -m "Release v1.0.3"
   git push origin v1.0.3
   ```

The workflow builds with `uv build --no-sources`, smoke-imports the wheel and sdist, then runs `uv publish` using OIDC (no API token in secrets).

Manual upload from your machine is still possible: `uv build` then `UV_PUBLISH_TOKEN=pypi-... uv publish`.

## Contributing

Issues and pull requests are welcome. Please run `uv run ruff check`, `uv run ruff format --check`, and `uv run pytest` before submitting a change.

## License

MIT — see [LICENSE](LICENSE).
