from typing import Type
from app.core.models.task_model import TaskModel
from app.core.entities.task_entity import TaskEntity


def map_task_model_to_entity(task_instance: Type[TaskModel]) -> TaskEntity:
    return TaskEntity(
        id=task_instance.id,
        title=task_instance.title,
        description=task_instance.description,
        is_completed=task_instance.is_completed,
        created_at=task_instance.created_at,
        deadline=task_instance.deadline,
    )
