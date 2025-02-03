from ..task_repository import TaskRepository
from sqlalchemy.orm import Session
from app.core.models.task_model import TaskModel
from ..task_repository import TaskEntity
from typing import Type
from app.core.mappers import map_task_model_to_entity


class TaskPSQLRepository(TaskRepository):
    def __init__(self, session_instance: Session) -> None:
        self.session_instance = session_instance
        self.model_class: Type[TaskModel] = TaskModel

    def get_all_tasks(self) -> list[TaskEntity]:
        tasks: list[Type[TaskModel]] = self.session_instance.query(self.model_class).all()
        return [map_task_model_to_entity(task) for task in tasks]

    def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        task: Type[TaskModel] | None = self.session_instance.query(self.model_class).get(id_value)
        if task:
            return map_task_model_to_entity(task)
        return None
