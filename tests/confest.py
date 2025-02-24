import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

from logger import logger

env_path = Path(__file__).parent / ".env.test"
load_dotenv(env_path)


@pytest.fixture(scope="session", autouse=True)
def set_test_env():
    print(f"ASYNC_DATABASE_URL: {os.getenv('ASYNC_DATABASE_URL')}")
    os.environ["ASYNC_DATABASE_URL"] = os.getenv(
        "ASYNC_DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
    )
    print(f"ASYNC_DATABASE_URL: {os.getenv('ASYNC_DATABASE_URL')}")
