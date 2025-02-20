from app.core.repositories.impl.task_psql_repository import TaskPSQLRepository
from app.core.repositories.task_repository import TaskRepository


def production_config(binder):
    binder.bind(TaskRepository, TaskPSQLRepository)
