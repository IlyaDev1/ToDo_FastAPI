import pytest

from app.core.entities.task_entity import TaskEntity
from app.core.service.db_service import TaskService


class TestTaskCompletedService:
    """Здесь будут тесты для функции сервиса отметить таску как выполненную"""

    @pytest.mark.asyncio
    async def test_task_not_found(self, task_service: TaskService):
        """Если сервис не видит задачу, то он должен вернуть None"""

        response = await task_service.mark_task_completed(-1)  # type: ignore
        # Задачи с id=-1 быть не может по ограничениям pk
        assert response is None

    @pytest.mark.asyncio
    async def test_task_completed(
        self,
        task_service: TaskService,
        create_task_and_get_id: str,
    ):
        """Это тест на то, что сервис возвращает entity задачи с is_completed=True"""

        response: TaskEntity = await task_service.mark_task_completed(create_task_and_get_id)  # type: ignore
        assert response.is_completed
