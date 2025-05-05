import pytest
from httpx import AsyncClient

from app.api.routes.v1.task import task_completed  # type: ignore
from app.core.entities.task_entity import TaskEntity


class TestTaskCompleted:
    """Тесты для ручки, которая отмечает задачу выполненной"""

    @pytest.mark.asyncio
    async def test_task_completed(self, create_task_and_get_id: str):
        """Этот интеграционных тест проверяет, что роутер имеет такую функцию"""

        response: TaskEntity = await task_completed(create_task_and_get_id)

        assert response.is_completed
