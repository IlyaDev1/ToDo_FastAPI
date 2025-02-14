from abc import ABC, abstractmethod

from app.core.dtos.task_dto import TaskDTO
from app.core.entities.task_entity import TaskEntity


class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[TaskEntity]: ...

    @abstractmethod
    def get_task_by_id(self, id_value: int) -> TaskEntity | None: ...

    @abstractmethod
    def create_task(self, task: TaskDTO) -> TaskEntity: ...

    @abstractmethod
    def delete_task_by_id(self, id_value: int) -> TaskEntity | None: ...
