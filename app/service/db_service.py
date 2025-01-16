from app.repositories.task_repository import TaskRepository
from app.models.task_model import TaskModel
from app.core.dependencies import get_db
from app.entities.task_entity import TaskEntity
from fastapi import Depends
from inject import instance


class TaskService:
    def __init__(self) -> None:
        self.task_psql_repo: TaskRepository = instance(TaskRepository)

    def get_all_tasks(self) -> list[TaskEntity]:
        return self.task_psql_repo.get_all_tasks()
