import asyncio
import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from httpx import ASGITransport, AsyncClient

from app.core.database import engine, sync_engine
from app.core.models.base import Base
from app.core.models.task_model import TaskModel
from app.main import app

load_dotenv()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def setup_db_sync():
    assert os.getenv("MODE") == "TEST", "Ты используешь не тестовую БД"

    with sync_engine.begin() as conn:
        Base.metadata.drop_all(bind=conn)
        Base.metadata.create_all(bind=conn)

    yield

    with sync_engine.begin() as conn:
        Base.metadata.drop_all(bind=conn)


@pytest_asyncio.fixture(scope="session")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
