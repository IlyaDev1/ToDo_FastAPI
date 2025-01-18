from app.repositories.task_repository import TaskRepository
from app.entities.task_entity import TaskEntity
from inject import instance


class TaskService:
    def __init__(self) -> None:
        self.task_repo: TaskRepository = instance(TaskRepository)

    def get_all_tasks(self) -> list[TaskEntity]:
        return self.task_repo.get_all_tasks()
