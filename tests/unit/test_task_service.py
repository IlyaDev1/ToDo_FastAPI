from copy import copy
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.core.entities.task_entity import TaskEntity
from app.core.service.db_service import TaskService


@pytest.mark.asyncio
async def test_task_completed(monkeypatch, task_entity_instance: TaskEntity):
    """Could mark task as completed."""

    fake_task: TaskEntity = copy(task_entity_instance)
    fake_completed_task: TaskEntity = TaskEntity(
        id=1,
        title="title",
        description="desc",
        is_completed=True,
        created_at=fake_task.created_at,
        deadline=None,
    )

    mock_repo = MagicMock()
    mock_repo.get_task_by_id = AsyncMock(return_value=fake_task)
    mock_repo.change_instance = AsyncMock(return_value=fake_completed_task)

    monkeypatch.setattr("app.core.service.db_service.instance", lambda _: mock_repo)

    service = TaskService()

    result = await service.mark_task_completed(task_id=1)  # type: ignore

    assert result == fake_completed_task
    mock_repo.get_task_by_id.assert_called_once()
    mock_repo.change_instance.assert_called_once()
