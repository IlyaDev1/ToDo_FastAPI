import asyncio
import os
from datetime import datetime, timedelta

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from httpx import ASGITransport, AsyncClient

from app.core.database import engine
from app.core.dtos.task_dto import TaskDTO
from app.core.models.base import Base
from app.core.models.task_model import TaskModel
from app.main import app
from tests.constants import TASK_URL

load_dotenv()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def setup_db():
    assert os.getenv("MODE") == "TEST", "Ты берешь не тестовую БД"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="session")
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest_asyncio.fixture(scope="function")
async def create_task_and_get_id(
    async_client: AsyncClient, task_for_create: TaskDTO
) -> str:
    """Фикстура для создания новой задачи и отдача ее id"""

    response = await async_client.post(TASK_URL, json=task_for_create.to_json())
    assert response.status_code == 201, "Проблема с созданием задачи"

    return response.json()["id"]


@pytest_asyncio.fixture(scope="function")
async def task_for_create() -> TaskDTO:
    return TaskDTO(
        title="title",
        description="description",
        deadline=datetime.now() + timedelta(days=1),
        is_completed=False,
        created_at=datetime.now(),
    )
