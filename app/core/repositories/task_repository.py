from abc import ABC, abstractmethod
from app.core.entities.task_entity import TaskEntity
from typing import Union


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[TaskEntity]:
        ...

    @abstractmethod
    def get_task_by_id(self, id_value: int) -> Union[TaskEntity, None]:
        ...
