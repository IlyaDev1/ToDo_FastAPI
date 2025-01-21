from .dependencies import get_db
from app.repositories.task_repository import TaskRepository
from app.repositories.impl.task_psql_repository import TaskPSQLRepository


def production_config(binder):
    with get_db() as db:
        binder.bind(TaskRepository, TaskPSQLRepository(db))
