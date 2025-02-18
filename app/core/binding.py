from app.core.repositories.impl.task_psql_repository import TaskPSQLRepository
from app.core.repositories.task_repository import TaskRepository

from .dependencies import get_db


async def production_config(binder):
    async with get_db() as db:
        binder.bind(TaskRepository, TaskPSQLRepository(db))
