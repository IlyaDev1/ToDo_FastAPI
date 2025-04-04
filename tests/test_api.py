from datetime import datetime, timedelta

import pytest
from httpx import ASGITransport, AsyncClient

from app.api.schemas.task import TaskCreate
from app.main import app


@pytest.mark.asyncio
class TestCreateTaskAPI:
    async def test_create_task_success(self):
        """Проверяем успешное создание задачи"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            task_data = {
                "title": "Test Task",
                "description": "This is a test task",
                "deadline": (datetime.utcnow() + timedelta(days=7)).isoformat(),
            }
            response = await ac.post("/api/v1/task/", json=task_data)
            assert response.status_code == 200
            assert response.json()["title"] == task_data["title"]

    async def test_create_task_missing_title(self):
        """Проверяем создание задачи без заголовка (должна быть ошибка)"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            task_data = {
                "description": "Missing title",
                "deadline": (datetime.now() + timedelta(days=7)).isoformat(),
            }
            response = await ac.post("/api/v1/task/", json=task_data)
            assert response.status_code == 422  # Ошибка валидации

    async def test_create_task_invalid_deadline(self):
        """Проверяем создание задачи с некорректным форматом даты"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            task_data = {
                "title": "Invalid Deadline",
                "description": "Wrong format",
                "deadline": "invalid-date-format",
            }
            response = await ac.post("/api/v1/task/", json=task_data)
            assert response.status_code == 422  # Ошибка валидации

    async def test_create_task_without_deadline(self):
        """Проверяем создание задачи без дедлайна (должно пройти)"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            task_data = {
                "title": "No Deadline Task",
                "description": "Task without deadline",
            }
            response = await ac.post("/api/v1/task/", json=task_data)
            assert response.status_code == 200
            assert response.json()["title"] == task_data["title"]

    async def test_create_task_empty_body(self):
        """Проверяем создание задачи с пустым телом запроса (должна быть ошибка)"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            response = await ac.post("/api/v1/task/", json={})
            assert response.status_code == 422  # Ошибка валидации
