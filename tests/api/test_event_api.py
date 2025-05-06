import pytest
from httpx import AsyncClient

from tests.constants import EVENTS_URL


@pytest.mark.asyncio
async def test_get_all_events(async_client: AsyncClient):
    """Тест проверяет, что по ручке можно обратиться к url события и оно вернет хотя бы статус 200"""

    response = await async_client.get(EVENTS_URL)
    assert response.status_code == 200
