from abc import ABC, abstractmethod
from app.core.dtos.task_dto import TaskDTO


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[TaskDTO]:
        ...

    @abstractmethod
    def get_task_by_id(self, id_value: int) -> TaskDTO | None:
        ...
