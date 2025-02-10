from abc import ABC, abstractmethod
from app.core.entities.task_entity import TaskEntity
from app.core.dtos.task_dto import TaskDTO


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[TaskEntity]:
        ...

    @abstractmethod
    def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        ...

    @abstractmethod
    def create_task(self, task: TaskDTO) -> TaskEntity:
        ...

    @abstractmethod
    def delete_task_by_id(self, id_value: int) -> TaskEntity | None:
        ...
