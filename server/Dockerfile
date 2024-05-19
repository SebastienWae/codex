FROM 3.12.3-slim-bookworm

COPY poetry.lock pyproject.toml /app/

WORKDIR /app

# install poetry
RUN pip install poetry

# install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev