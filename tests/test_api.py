from copy import deepcopy
from datetime import datetime, timedelta

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient, Response

from app.core.dtos.task_dto import TaskDTO
from app.main import app
from tests.constants import (
    CHANGE_DEADLINE_URL,
    CURRENT_TIMESTAMP,
    TASK_DTO_INSTANCE,
    TASK_URL,
)


@pytest.mark.asyncio
async def test_get_all_tasks(async_client: AsyncClient):
    """Это тест, который показывает, что система минимально работает"""
    response = await async_client.get(TASK_URL)
    assert response.status_code == 200


class TestCreateTask:
    """Класс тестов для создания задачи"""

    MAX_TITLE_LENGTH = 60

    @pytest.mark.asyncio
    async def test_create_task_with_empty_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с пустым title полем, так делать нельзя по нашей бизнес-логике"""
        # Я ожидаю http ответ со статус кодом 422, потому что нужна в таком случае обработка на уровне парсинга данных pydantic(ом)

        task_instance: TaskDTO = deepcopy(TASK_DTO_INSTANCE)

        task_instance.title = ""

        response = await async_client.post(TASK_URL, json=task_instance.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_too_long_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с title больше 60, так нельзя по нашей бузинес-логике"""
        # Я ожидаю, что дропнется http со статус кодом 422, чтобы обработка была на уровне pydantic

        too_long_title = "a" * (TestCreateTask.MAX_TITLE_LENGTH + 1)

        task_instance: TaskDTO = deepcopy(TASK_DTO_INSTANCE)

        task_instance.title = too_long_title

        response = await async_client.post(TASK_URL, json=task_instance.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_60_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с title 60, так как это можно по нашей бузинес-логике (крайний случай)"""
        # Я ожидаю, что дропнется http со статус кодом 201

        extreme_title = "a" * TestCreateTask.MAX_TITLE_LENGTH

        task_instance: TaskDTO = deepcopy(TASK_DTO_INSTANCE)

        task_instance.title = extreme_title

        response = await async_client.post(TASK_URL, json=task_instance.to_json())
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_empty_deadline(self, async_client: AsyncClient):
        """Пытаюсь создать задачу с deadline null, так должно быть можно"""
        # Ожидаю 201

        task_instance: TaskDTO = deepcopy(TASK_DTO_INSTANCE)
        task_instance.deadline = None

        response = await async_client.post(TASK_URL, json=task_instance.to_json())
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_deadline_before_current_time(self, async_client: AsyncClient):
        """Пытаюсь создать задачу с дедлайном раньше текущего времени, так не должно быть"""
        # Ожидаю 400

        task_instance = deepcopy(TASK_DTO_INSTANCE)
        task_instance.deadline = CURRENT_TIMESTAMP - timedelta(days=1)

        response = await async_client.post(TASK_URL, json=task_instance.to_json())
        assert response.status_code == 400


class TestChangeDeadline:
    """Класс посвящен тестам для ручки изменения дедлайна"""

    @pytest.mark.asyncio
    async def test_deadline_in_past(self, async_client: AsyncClient):
        """Пользователь хочет изменить дедлайн и ставит его в прошлое, так нельзя"""
        # Ожидаю 400

        task_for_create_instance = deepcopy(TASK_DTO_INSTANCE)

        create_task_response: Response = await async_client.post(
            TASK_URL, json=task_for_create_instance.to_json()
        )

        assert create_task_response.status_code == 201, "Проблема с созданием задачи"
        task_id = create_task_response.json()["id"]

        new_deadline: str = (CURRENT_TIMESTAMP - timedelta(days=1)).isoformat()

        url = f"{CHANGE_DEADLINE_URL}{task_id}"
        response = await async_client.patch(url, json={"deadline": new_deadline})
        assert response.status_code == 400
