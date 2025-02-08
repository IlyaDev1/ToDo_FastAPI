from ..task_repository import TaskRepository
from sqlalchemy.orm import Session
from app.core.models.task_model import TaskModel
from app.core.entities.task_entity import TaskEntity
from typing import Type


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
        task: TaskModel | None = self.session_instance.query(self.model_class).get(id_value)
        if task:
            return map_task_model_to_entity(task)
        return None
