FROM python:3
COPY . /workspace/.
WORKDIR /workspace

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-ansi --no-root
RUN poetry run tox
