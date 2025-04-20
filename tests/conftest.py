import asyncio
import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv

from app.core.database import engine
from app.core.models.base import Base
from app.core.models.task_model import TaskModel

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db():
    assert os.getenv("MODE") == "TEST", "Ты берешь не тестовую БД"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
