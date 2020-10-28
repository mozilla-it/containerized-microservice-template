## Developer Setup
Technologies used: poetry, pre-commit, ...

### Poetry Setup
Install Poetry for osx/linux:
* `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

Install all no-dev dependencies in pyproject.toml through poetry:
* `poetry install --no-dev`

Install ALL deps including DEV env dependencies:
* `poetry install `

Opens shell with corresponding dependencies to the poetry(.lock) in the directory that you make the call:
* `poetry shell`

Runs command with poetry venv:
* `poetry run {command}`

### Install Pre-commit

Using poetry (pre-commit is located in the [Pyproject.toml](../pyproject.toml) )
* `poetry shell`
* `pre-commit install`

You should get the following response after installing pre-commit:

>`pre-commit installed at .git/hooks/pre-commit`

### Pre-commit, Run on the Entire Codebase

Run the following command where you installed pre-commit.
* `pre-commit run --all-files`

### Exiting Poetry Shell

Run the following command to exit `poetry shell` while in a shell.
* `exit`

The command `deactivate` will not work to full disengage the poetry shell as it does with `venv`.
