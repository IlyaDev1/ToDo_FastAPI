from app.core.repositories.task_repository import TaskRepository
from app.core.dtos.task_dto import TaskDTO
from app.api.schemas.todo import TaskBase
from inject import instance
from typing import Union


def map_task_dto_to_pydantic(task_dto_instance: TaskDTO) -> TaskBase:
    return TaskBase(
        id=task_dto_instance.id,
        title=task_dto_instance.title,
        description=task_dto_instance.description,
        is_completed=task_dto_instance.is_completed,
        created_at=task_dto_instance.created_at,
        deadline=task_dto_instance.deadline,
    )


class TaskService:
    def __init__(self) -> None:
        self.task_repo: TaskRepository = instance(TaskRepository)

    def get_all_tasks(self) -> list[TaskBase]:
        tasks_dto = self.task_repo.get_all_tasks()
        return [map_task_dto_to_pydantic(task_dto) for task_dto in tasks_dto]

    def get_task_by_id(self, id_value: int) -> TaskBase | None:
        result = self.task_repo.get_task_by_id(id_value)
        if result:
            return map_task_dto_to_pydantic(result)
        return None
