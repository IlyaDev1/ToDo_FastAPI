from app.repositories.impl.task_psql_repository import TaskPSQLRepository
from app.models.task_model import TaskModel
from app.core.dependencies import get_db
from app.entities.task_entity import TaskEntity
from fastapi import Depends


class TaskService:
    def __init__(self) -> None:
        self.task_psql_repo: TaskPSQLRepository = TaskPSQLRepository(Depends(get_db))

    def get_all_tasks(self) -> list[TaskEntity]:
        return self.task_psql_repo.get_all_tasks()
