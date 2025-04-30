from copy import deepcopy
from datetime import datetime, timedelta

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.core.dtos.task_dto import TaskDTO
from app.main import app

task_url = "/api/v1/task/"  # Я делаю глобальную, потому что в будущем я буду разбивать test_api на разные модули
# Когда будет больше сущностей
# Для каждого эндпоинта - один модуль ->
# в каждом модуле будет глобальная переменная для url эндпоинта своя


@pytest_asyncio.fixture(scope="function")
async def task_for_create() -> TaskDTO:
    return TaskDTO(
        title="title",
        description="description",
        deadline=datetime.now() + timedelta(days=1),
        is_completed=False,
        created_at=datetime.now(),
    )


@pytest_asyncio.fixture(scope="function")
async def create_task_and_get_id(
    async_client: AsyncClient, task_for_create: TaskDTO
) -> str:
    """Фикстура для создания новой задачи и отдача ее id"""

    response = await async_client.post(task_url, json=task_for_create.to_json())
    assert response.status_code == 201, "Проблема с созданием задачи"

    return response.json()["id"]


@pytest.mark.asyncio
async def test_get_all_tasks(async_client: AsyncClient):
    """Это тест, который показывает, что система минимально работает"""
    response = await async_client.get(task_url)
    assert response.status_code == 200


class TestCreateTask:
    """Класс тестов для создания задачи"""

    max_title_length = 60

    @pytest.mark.asyncio
    async def test_create_task_with_empty_title(
        self, async_client: AsyncClient, task_for_create: TaskDTO
    ):
        """Мы пытаемся создать задачу с пустым title полем, так делать нельзя по нашей бизнес-логике"""
        # Я ожидаю http ответ со статус кодом 422, потому что нужна в таком случае обработка на уровне парсинга данных pydantic(ом)

        task_for_create.title = ""

        response = await async_client.post(task_url, json=task_for_create.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_too_long_title(
        self, async_client: AsyncClient, task_for_create: TaskDTO
    ):
        """Мы пытаемся создать задачу с title больше 60, так нельзя по нашей бузинес-логике"""
        # Я ожидаю, что дропнется http со статус кодом 422, чтобы обработка была на уровне pydantic

        too_long_title = "a" * (TestCreateTask.max_title_length + 1)
        task_for_create.title = too_long_title

        response = await async_client.post(task_url, json=task_for_create.to_json())
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_create_task_with_60_title(
        self, async_client: AsyncClient, task_for_create: TaskDTO
    ):
        """Мы пытаемся создать задачу с title 60, так как это можно по нашей бузинес-логике (крайний случай)"""
        # Я ожидаю, что дропнется http со статус кодом 201

        extreme_title = "a" * TestCreateTask.max_title_length
        task_for_create.title = extreme_title

        response = await async_client.post(task_url, json=task_for_create.to_json())
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_empty_deadline(
        self, async_client: AsyncClient, task_for_create: TaskDTO
    ):
        """Пытаюсь создать задачу с deadline null, так должно быть можно"""
        # Ожидаю 201

        task_for_create.deadline = None

        response = await async_client.post(task_url, json=task_for_create.to_json())
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_deadline_before_current_time(
        self, async_client: AsyncClient, task_for_create: TaskDTO
    ):
        """Пытаюсь создать задачу с дедлайном раньше текущего времени, так не должно быть"""
        # Ожидаю 422

        task_for_create.deadline = datetime.now() - timedelta(days=1)
        response = await async_client.post(task_url, json=task_for_create.to_json())
        assert response.status_code == 422


class TestChangeDeadline:
    """Класс посвящен тестам для ручки изменения дедлайна"""

    @staticmethod
    def get_url_with_id(task_id: str | int) -> str:
        return f"{task_url}rearrange/{task_id}"

    @pytest.mark.asyncio
    async def test_deadline_in_past(
        self,
        async_client: AsyncClient,
        create_task_and_get_id: str,
    ):
        """Пользователь хочет изменить дедлайн и ставит его в прошлое, так нельзя"""
        # Ожидаю 422

        new_deadline: str = (datetime.now() - timedelta(days=1)).isoformat()

        url = self.get_url_with_id(create_task_and_get_id)
        response = await async_client.patch(url, json={"deadline": new_deadline})
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_empty_deadline(
        self, async_client: AsyncClient, create_task_and_get_id: str
    ):
        """Если пользователь ставит новый дедлайн в None, то ошибок не должно быть"""
        # Ожидаю, что у задачи, deadline, действительно, None

        new_deadline = None

        url = self.get_url_with_id(create_task_and_get_id)
        response = await async_client.patch(url, json={"deadline": new_deadline})
        assert response.json()["deadline"] is None


class TestTaskCompleted:
    """Здесь будут тесты для функций завершенности таски"""

    @staticmethod
    def get_endpoint_url(task_id: str | int) -> str:
        return f"{task_url}completed/{task_id}"

    @pytest.mark.asyncio
    async def test_task_not_completed_after_creation(
        self,
        async_client: AsyncClient,
        create_task_and_get_id: str,
    ):
        """Будет проверяться, что у задачи сразу после создания не может быть таска сразу выполнена"""

        current_task_url = f"{task_url}{create_task_and_get_id}"

        task_response = await async_client.get(current_task_url)

        assert task_response.status_code == 200
        assert not task_response.json()["is_completed"]

    @pytest.mark.asyncio
    async def test_task_completed(
        self, async_client: AsyncClient, create_task_and_get_id: str
    ):
        """Этот тест будет проверять, что после установки таски как выполненной, is_completed = True"""

        endpoint_url = self.get_endpoint_url(create_task_and_get_id)

        response = await async_client.patch(endpoint_url)
        assert response.status_code == 200
