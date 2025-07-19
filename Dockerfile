FROM python:3.12-slim

WORKDIR /todo

RUN pip install --no-cache-dir uv

COPY uv.lock pyproject.toml /todo/

RUN uv sync --frozen --no-cache

COPY . /todo/

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/todo

CMD uv run alembic upgrade head && uv run python app/main.py
