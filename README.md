# transliteration-ua

[![Build Status](https://github.com/yakimka/transliteration-ua/actions/workflows/workflow-ci.yml/badge.svg?branch=main&event=push)](https://github.com/yakimka/transliteration-ua/actions/workflows/workflow-ci.yml)
[![Codecov](https://codecov.io/gh/yakimka/transliteration-ua/branch/main/graph/badge.svg)](https://codecov.io/gh/yakimka/transliteration-ua)
[![PyPI - Version](https://img.shields.io/pypi/v/transliteration-ua.svg)](https://pypi.org/project/transliteration-ua/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/transliteration-ua)](https://pypi.org/project/picodi/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/transliteration-ua)](https://pypi.org/project/picodi/)

Ukrainian transliteration by official rules


## CI\CD Note (delete this section)

For properly running CI/CD, you must set the following environment secrets in repo settings:

- `DOCKERHUB_TOKEN`
- `PYPI_TOKEN`
- `CODECOV_TOKEN`
- `UPDATE_URL` for [updater](https://github.com/umputun/updater)

## Installation

```bash
pip install transliteration-ua
```

## Example

Showcase how your project can be used:

```python
from transliteration_ua.example import some_function

print(some_function(3, 4))
# => 7
```

## Docker images

Docker images (amd64 and arm64) are available on
[Docker Hub](https://hub.docker.com/r/yakimka/transliteration-ua).

## Development

### Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. (?) Copy the example settings file and configure your settings:
   ```bash
   cp settings.example.yaml settings.yaml
   ```
3. Build the Docker images:
   ```bash
   docker-compose build
   ```
4. Install dependencies:
   ```bash
   make poetry args="install"
   ```
5. Start the service:
   ```bash
   docker-compose up
   ```

### Making Changes

1. List available `make` commands:
   ```bash
   make help
   ```
2. Check code style with:
   ```bash
   make lint
   ```
3. Run tests using:
   ```bash
   make test
   ```
4. Manage dependencies via Poetry:
   ```bash
   make poetry args="<poetry-args>"
   ```
   - For example: `make poetry args="add picodi"`

5. For local CI debugging:
   ```bash
   make run-ci
   ```

#### Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) for linting and formatting:
- It runs inside a Docker container by default.
- Optionally, set up hooks locally:
  ```bash
  pre-commit install
  ```

#### Mypy

We use [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking.

It is configured for strictly typed code, so you may need to add type hints to your code.
But don't be very strict, sometimes it's better to use `Any` type.

## License

[MIT](https://github.com/yakimka/transliteration-ua/blob/main/LICENSE)


## Credits

This project was generated with [`yakimka/cookiecutter-pyproject`](https://github.com/yakimka/cookiecutter-pyproject).
