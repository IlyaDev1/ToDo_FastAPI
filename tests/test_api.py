import os

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
@pytest.mark.usefixtures("setup_db")
class APITests:
    async def async_client(self):
        """Возвращаем асинхронный клиент для асинхронных тестов"""
        return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")

    async def test_service_is_alive(self):
        """Проверяем, что сервер запущен, отдает хоть что-то"""
        async with self.async_client() as ac:
            response = await ac.get("/api/v1/task/")
            assert response.status_code == 200
