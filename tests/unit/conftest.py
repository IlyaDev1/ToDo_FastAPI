from datetime import datetime

import pytest

from app.core.entities.task_entity import TaskEntity


@pytest.fixture(scope="package")
def task_entity_instance() -> TaskEntity:
    """Get task entity."""

    return TaskEntity(
        id=1,
        title="title",
        description="desc",
        is_completed=False,
        created_at=datetime.now(),
        deadline=None,
    )
