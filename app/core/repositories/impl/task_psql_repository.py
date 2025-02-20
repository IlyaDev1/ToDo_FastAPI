from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.dependencies import get_db
from app.core.entities.task_entity import TaskEntity
from app.core.models.task_model import TaskModel

from ...dtos.task_dto import TaskDTO
from ..task_repository import TaskRepository


def map_task_model_to_entity(task_instance: TaskModel) -> TaskEntity:
    return TaskEntity(
        id=task_instance.id,
        title=task_instance.title,
        description=task_instance.description,
        is_completed=task_instance.is_completed,
        created_at=task_instance.created_at,
        deadline=task_instance.deadline,
    )


async def get_task_by_id_or_none(
    session_instance: AsyncSession, id_value: int
) -> TaskModel | None:
    stmt = select(TaskModel).where(TaskModel.id == id_value)
    result = await session_instance.execute(stmt)
    return result.scalar_one_or_none()


class TaskPSQLRepository(TaskRepository):
    def __init__(self) -> None:
        self.model_class: Type[TaskModel] = TaskModel

    async def get_all_tasks(self) -> list[TaskEntity]:
        async with get_db() as session_instance:
            stmt = select(self.model_class)
            result = await session_instance.execute(stmt)
            tasks = result.scalars().all()
            return [map_task_model_to_entity(task) for task in tasks]

    async def get_task_by_id(self, id_value: int) -> TaskEntity | None:
        async with get_db() as session_instance:
            task = await get_task_by_id_or_none(session_instance, id_value)
            if task:
                return map_task_model_to_entity(task)
            return None

    async def create_task(self, task: TaskDTO) -> TaskEntity:
        async with get_db() as session_instance:
            task = TaskModel(
                title=task.title,
                description=task.description,
                deadline=task.deadline.replace(tzinfo=None),  # type: ignore
            )
            session_instance.add(task)
            await session_instance.commit()
            return map_task_model_to_entity(task)

    async def delete_task_by_id(self, id_value: int) -> TaskEntity | None:
        async with get_db() as session_instance:
            task_instance = await get_task_by_id_or_none(session_instance, id_value)
            if task_instance:
                task_entity_instance = map_task_model_to_entity(task_instance)
                await session_instance.delete(task_instance)
                await session_instance.commit()
                return task_entity_instance
            return None

    async def change_instance(self, task: TaskEntity) -> TaskEntity | None:
        async with get_db() as session_instance:
            task_model_instance = await get_task_by_id_or_none(
                session_instance, task.id
            )
            if task_model_instance:
                task_model_instance.title = task.title
                task_model_instance.description = task.description
                task_model_instance.is_completed = task.is_completed
                task_model_instance.created_at = task.created_at
                task_model_instance.deadline = task.deadline.replace(tzinfo=None)  # type: ignore
                await session_instance.commit()
                return map_task_model_to_entity(task_model_instance)
            return None
