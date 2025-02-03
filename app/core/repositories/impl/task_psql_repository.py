from ..task_repository import TaskRepository
from sqlalchemy.orm import Session
from app.core.models.task_model import TaskModel
from ..task_repository import TaskEntity
from typing import Type, Union


class TaskPSQLRepository(TaskRepository):
    def __init__(self, session_instance: Session) -> None:
        self.session_instance = session_instance
        self.model_class: Type[TaskModel] = TaskModel

    def get_all_tasks(self) -> list[TaskEntity]:
        tasks: list[Type[TaskModel]] = self.session_instance.query(self.model_class).all()
        return [
            TaskEntity(
                id=task.id,
                title=task.title,
                description=task.description,
                is_completed=task.is_completed,
                created_at=task.created_at,
                deadline=task.deadline,
            )
            for task in tasks]

    def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        task = self.session_instance.query(self.model_class).get(id_value)
        if task:
            return TaskEntity(
                id=task.id,
                title=task.title,
                description=task.description,
                is_completed=task.is_completed,
                created_at=task.created_at,
                deadline=task.deadline,
            )
        return None
