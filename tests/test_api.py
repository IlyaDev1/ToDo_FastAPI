import os
from dataclasses import asdict
from datetime import datetime

import pytest
from httpx import ASGITransport, AsyncClient

from app.core.dtos.task_dto import TaskDTO
from app.main import app

task_url = "/api/v1/task/"


@pytest.mark.asyncio
async def test_get_all_tasks(async_client: AsyncClient):
    """Это тест, который показывает, что система минимально работает"""
    response = await async_client.get(task_url)
    assert response.status_code == 200


class TestCreateTask:
    """Класс тестов для создания задачи"""

    max_title_length = 60

    @pytest.mark.asyncio
    async def test_create_task_with_empty_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с пустым title полем, так делать нельзя по нашей бизнес-логике"""
        # Я ожидаю http ответ со статус кодом 422, потому что нужна в таком случае обработка на уровне парсинга данных pydantic(ом)
        payload = TaskDTO(
            title="",
            description="description",
            deadline=datetime(2025, 10, 10, 5, 1, 1),
            is_completed=False,
            created_at=None,
        )
        response = await async_client.post(task_url, json=payload.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_too_long_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с title больше 60, так нельзя по нашей бузинес-логике"""
        # Я ожидаю, что дропнется http со статус кодом 422, чтобы обработка была на уровне pydantic

        too_long_title = "a" * (TestCreateTask.max_title_length + 1)
        payload = TaskDTO(
            title=too_long_title,
            description="description",
            deadline=datetime(2025, 10, 10, 5, 1, 1),
            is_completed=False,
            created_at=None,
        )
        response = await async_client.post(task_url, json=payload.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_60_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с title 60, так как это можно по нашей бузинес-логике (крайний случай)"""
        # Я ожидаю, что дропнется http со статус кодом 201

        extreme_title = "a" * TestCreateTask.max_title_length
        payload = TaskDTO(
            title=extreme_title,
            description="description",
            deadline=datetime(2025, 10, 10, 5, 1, 1),
            is_completed=False,
            created_at=None,
        )
        response = await async_client.post(task_url, json=payload.to_json())
        assert response.status_code == 201
