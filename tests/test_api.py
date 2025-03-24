import os

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
class TestAPI:
    @pytest.fixture()
    async def get_async_client(self):
        """Возвращаем асинхронный клиент для асинхронных тестов"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            yield ac

    async def test_service_is_alive(self, async_client):
        """Проверяем, что сервер запущен, отдает хоть что-то"""
        response = await async_client.get("/api/v1/task/")
        assert response.status_code == 200
