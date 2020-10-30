## Developer Setup
Technologies used: poetry, pre-commit, ...

---
## Poetry

## Installation
Install Poetry for osx/linux:
> `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

Install prod dependencies in pyproject.toml through poetry:
> `poetry install --no-dev`

Install ALL deps including DEV dependencies:
> `poetry install `

### In Use
Opens shell with corresponding dependencies to the poetry(.lock) in the directory that you make the call:
> `poetry shell`
< Provides access to all the dependencies installed

Runs command with poetry venv:
> `poetry run {command}`

### Adding Dependencies
Add new dependencies in pyproject.toml through poetry:
> `poetry add {pypi-package}`

[...view poetry site for further documentation and details.](https://python-poetry.org/)

### Exiting Poetry Shell

Run the following command to exit `poetry shell` while in a shell.
> `exit`

The command `deactivate` will not work to full disengage the poetry shell as it does with `venv`.

---
## Pre-commit

### Installation
Using poetry (pre-commit is located in the [pyproject.toml](../pyproject.toml) )
> `poetry shell`
> `pre-commit install`

You should get the following response after installing pre-commit into the githooks:

>`pre-commit installed at .git/hooks/pre-commit`

### Pre-commit, Run on the Entire Codebase

Run the following command where you installed pre-commit.
> `pre-commit run --all-files`

## Docker

### Installation
Install Docker here: https://docs.docker.com/get-docker/

### Building
Build images with:
> `docker build --tag containerized_microservice_template --file docker/Dockerfile .`

Stop the build at optional stages (development, lint, test, production) with the --target option:
> `docker build --name containerized_microservice_template --file docker/Dockerfile . --target <stage>`

#### Optional
It is also possible to build the image through the provided scripts:
> poetry run scripts/build.sh
