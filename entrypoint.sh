#!/bin/bash
set -e

alembic revision --autogenerate -m "Initial migration" || true

alembic upgrade head

exec "$@"
