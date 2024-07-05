FROM python:3.11-buster AS builder

RUN pip install poetry==1.8.2 --no-cache-dir

WORKDIR /app

COPY pyproject.toml poetry.lock poetry.toml ./

RUN touch README.md && poetry install --without dev --no-root && rm -rf /tmp/poetry_cache


FROM python:3.11-slim-buster AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY random_bible_verse ./random_bible_verse

COPY bibles.db .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0", "random_bible_verse.app:server"]