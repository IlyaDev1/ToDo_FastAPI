from app.core.repositories.task_repository import TaskRepository
from inject import instance
from app.core.entities.task_entity import TaskEntity
from app.core.dtos.task_dto import TaskDTO


class TaskService:
    def __init__(self) -> None:
        self.task_repo = instance(TaskRepository)

    def get_all_tasks(self) -> list[TaskEntity]:
        tasks_dto = self.task_repo.get_all_tasks()
        return tasks_dto

    def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        result = self.task_repo.get_task_by_id(id_value)
        if result:
            return result
        return None

    def create_task(self, task: TaskDTO) -> TaskEntity:
        return self.task_repo.create_task(task)
