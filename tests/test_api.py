import os

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
class TestAPI:
    async def test_service_is_alive(self):
        """Проверяем, что сервер запущен, отдает хоть что-то"""
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            response = await ac.get("/api/v1/task/")
            assert response.status_code == 200
