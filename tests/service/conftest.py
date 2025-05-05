import pytest

from app.core.service.db_service import TaskService


@pytest.fixture(scope="session")
def task_service():
    task_service_instance = TaskService()
    yield task_service_instance
