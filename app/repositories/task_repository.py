from abc import ABC, abstractmethod
from app.entities.task_entity import TaskEntity


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[TaskEntity]:
        ...
