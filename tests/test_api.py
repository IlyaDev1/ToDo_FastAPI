import os

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_get_all_tasks():
    print(f"ASYNC_DATABASE_URL: {os.getenv('ASYNC_DATABASE_URL')}")
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/api/v1/task/")
        assert response.status_code == 200
