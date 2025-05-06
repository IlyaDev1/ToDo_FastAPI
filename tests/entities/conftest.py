from datetime import datetime

import pytest

from app.core.entities.task_entity import TaskEntity


@pytest.fixture(scope="function")
def task_entity_instance():
    """Фикстура должна отдать сущность задачи"""

    return TaskEntity(
        id=1,
        title="title",
        description="description",
        is_completed=False,
        created_at=datetime.now().replace(tzinfo=None),
        deadline=None,
    )
