import pytest

from app.core.database import engine
from app.core.models.base import Base
from app.core.models.task_model import TaskModel


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    for i in range(100):
        print("test")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
