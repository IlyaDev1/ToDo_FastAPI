from app.core.repositories.task_repository import TaskRepository
from app.core.entities.task_entity import TaskEntity
from inject import instance
from typing import Union


class TaskService:
    def __init__(self) -> None:
        self.task_repo: TaskRepository = instance(TaskRepository)

    def get_all_tasks(self) -> list[TaskEntity]:
        return self.task_repo.get_all_tasks()

    def get_task_by_id(self, id_value: int) -> Union[TaskEntity, None]:
        return self.task_repo.get_task_by_id(id_value)
