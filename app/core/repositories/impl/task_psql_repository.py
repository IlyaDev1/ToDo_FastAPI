from typing import Type

from sqlalchemy.orm import Session

from app.core.entities.task_entity import TaskEntity
from app.core.models.task_model import TaskModel

from ...dtos.task_dto import TaskDTO
from ..task_repository import TaskRepository


def map_task_model_to_entity(task_instance: TaskModel) -> TaskEntity:
    return TaskEntity(
        id=task_instance.id,
        title=task_instance.title,
        description=task_instance.description,
        is_completed=task_instance.is_completed,
        created_at=task_instance.created_at,
        deadline=task_instance.deadline,
    )


class TaskPSQLRepository(TaskRepository):
    def __init__(self, session_instance: Session) -> None:
        self.session_instance = session_instance
        self.model_class: Type[TaskModel] = TaskModel

    def get_all_tasks(self) -> list[TaskEntity]:
        tasks: list[TaskModel] = self.session_instance.query(self.model_class).all()
        return [map_task_model_to_entity(task) for task in tasks]

    def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        task: TaskModel | None = self.session_instance.query(self.model_class).get(
            id_value
        )
        if task:
            return map_task_model_to_entity(task)
        return None

    def create_task(self, task: TaskDTO) -> TaskEntity:
        task = TaskModel(
            title=task.title, description=task.description, deadline=task.deadline
        )
        self.session_instance.add(task)
        self.session_instance.commit()
        return map_task_model_to_entity(task)
