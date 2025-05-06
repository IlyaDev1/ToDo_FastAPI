import asyncio
import os
from datetime import datetime, timedelta

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from httpx import ASGITransport, AsyncClient

from app.core.database import sync_engine
from app.core.dtos.task_dto import TaskDTO
from app.core.models.base import Base
from app.core.models.task_model import TaskModel
from app.core.repositories.impl.task_psql_repository import TaskPSQLRepository
from app.main import app
from tests.constants import TASK_URL

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


@pytest_asyncio.fixture(scope="function")
async def create_task_and_get_id(
    async_client: AsyncClient, task_for_create: TaskDTO
) -> int:
    """Фикстура для создания новой задачи и отдача ее id"""

    response = await async_client.post(TASK_URL, json=task_for_create.to_json())
    assert response.status_code == 201, "Проблема с созданием задачи"

    return int(response.json()["id"])


@pytest_asyncio.fixture(scope="function")
async def task_for_create() -> TaskDTO:
    return TaskDTO(
        title="title",
        description="description",
        deadline=datetime.now() + timedelta(days=1),
        is_completed=False,
        created_at=datetime.now(),
    )
