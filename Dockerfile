FROM python:3.10-slim

WORKDIR /todo

RUN pip install --no-cache-dir uv

COPY requirements.txt /todo/

RUN uv pip install -r requirements.txt --system

COPY . /todo/

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/todo

CMD alembic upgrade head && python app/main.py
