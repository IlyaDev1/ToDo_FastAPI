from abc import ABC, abstractmethod

from app.core.dtos.task_dto import TaskDTO
from app.core.entities.task_entity import TaskEntity


class TaskRepository(ABC):
    @abstractmethod
    async def get_all_tasks(self) -> list[TaskEntity]: ...

    @abstractmethod
    async def get_task_by_id(self, id_value: int) -> TaskEntity | None: ...

    @abstractmethod
    async def create_task(self, task: TaskDTO) -> TaskEntity: ...

    @abstractmethod
    async def delete_task_by_id(self, id_value: int) -> TaskEntity | None: ...

    @abstractmethod
    async def change_instance(self, task: TaskEntity) -> TaskEntity | None:
        """Этот метод в моей голове должен делать следующее:
        Если у нас есть энтити задачи, который мы как-то меняли, то объект
        БД тоже надо поменять, поэтому этот метод это и делает, он принимает энтити,
        по его id находит объект из БД, меняет все атрибуты объекта из БД на атрибуты
        энтити и возвращает объект, переведенный из модели в entity
        """
        ...
