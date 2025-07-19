from datetime import datetime

from inject import instance

from app.core.dtos.task_dto import TaskDTO
from app.core.entities.task_entity import TaskEntity
from app.core.exceptions.task_exceptions import DeadlineInPastError
from app.core.repositories.task_repository import TaskRepository
from logger import logger


class TaskService:
    def __init__(self) -> None:
        self.task_repo = instance(TaskRepository)

    async def get_all_tasks(self) -> list[TaskEntity]:
        tasks_dto = await self.task_repo.get_all_tasks()
        return tasks_dto

    async def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        result = await self.task_repo.get_task_by_id(id_value)
        logger.info("Получение задачи по id")
        if result:
            return result
        return None

    async def create_task(self, task: TaskDTO) -> TaskEntity:
        if task.deadline is not None:
            task.deadline = task.deadline.replace(tzinfo=None)
            self.raise_if_deadline_in_past(task.deadline)
        return await self.task_repo.create_task(task)

    async def delete_task_by_id(self, task_id: int) -> TaskEntity | None:
        result = await self.task_repo.delete_task_by_id(task_id)
        if result:
            return result
        return None

    async def change_task_deadline(
        self, task_id: int, deadline: datetime | None
    ) -> TaskEntity | None:
        current_task = await self.task_repo.get_task_by_id(task_id)
        if not current_task:
            return None

        if deadline is not None:
            deadline = deadline.replace(tzinfo=None)
            self.raise_if_deadline_in_past(deadline)

        current_task.change_deadline(deadline)
        return await self.task_repo.change_instance(current_task)

    @staticmethod
    def raise_if_deadline_in_past(deadline: datetime) -> None:
        """Метод проверяет, что дедлайн не стоит в прошлом"""

        current_time = datetime.now()
        if deadline < current_time:
            raise DeadlineInPastError("Deadline must be in future")
