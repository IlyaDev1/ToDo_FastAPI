import pytest

from app.core.entities.task_entity import TaskEntity


class TestTaskEntity:
    """Тесты для сущности задачи"""

    def test_mark_task_completed(self, task_entity_instance: TaskEntity):
        """Тест проверяет, что можно поставить таску как выполненную (изменить атрибут is_completed на True)"""

        task_entity_instance.mark_task_completed()
        assert task_entity_instance.is_completed
