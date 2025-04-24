import os
from dataclasses import asdict
from datetime import datetime

import pytest
from httpx import ASGITransport, AsyncClient

from app.core.dtos.task_dto import TaskDTO
from app.main import app


@pytest.mark.asyncio
async def test_get_all_tasks(async_client: AsyncClient):
    """Это тест, который показывает, что система минимально работает"""
    response = await async_client.get("/api/v1/task/")
    assert response.status_code == 200


class TestCreateTask:
    """Класс тестов для создания задачи"""

    @pytest.mark.asyncio
    async def test_create_task_with_empty_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с пустым title полем, так делать нельзя по нашей бизнес-логике"""
        # Я ожидаю http ответ со статус кодом 422, потому что нужна в таком случае обработка на уровне парсинга данных pydantic(ом)
        payload: TaskDTO = TaskDTO(
            title="",
            description="description",
            deadline=datetime(2025, 10, 10, 5, 1, 1),
            is_completed=False,
            created_at=None,
        )
        response = await async_client.post("/api/v1/task/", json=payload.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_too_long_title(self, async_client: AsyncClient):
        """Мы пытаемся создать задачу с title больше 60, так нельзя по нашей бузинес-логике"""
        # Я ожидаю, что дропнется http со статус кодом 422, чтобы обработка была на уровне pydantic
        payload: TaskDTO = (
            TaskDTO(  # Я хочу создать в новом пуллрике фикстуру, отдающую payload, пока этого не делаю, так как хочу, чтобы пуллрики были максимально маленькими и соответствовали принципу единственной ответственности как бы говоря
                title="a" * 61,
                description="description",
                deadline=datetime(2025, 10, 10, 5, 1, 1),
                is_completed=False,
                created_at=None,
            )
        )
        response = await async_client.post(
            "/api/v1/task/", json=payload.to_json()
        )  # И еще я на уровне класса теста вынесу url в глобальную область видимости в некст пуллрике
        assert response.status_code == 422
