from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from inject import is_configured

from app.api.schemas.task import ChangeDeadline, TaskCreate
from app.core.dtos.task_dto import TaskDTO
from app.core.entities.task_entity import TaskEntity
from app.core.exceptions.task_exceptions import DeadlineInPastError
from app.core.service.db_service import TaskService
from logger import logger

from .responses import task_delete_response, task_not_found_response

tasks_router = APIRouter()

if is_configured():
    tasks_service = TaskService()


def map_task_pydantic_to_dto(task_pydantic_instance: TaskCreate):
    return TaskDTO(
        title=task_pydantic_instance.title,
        description=task_pydantic_instance.description,
        is_completed=False,
        created_at=None,
        deadline=task_pydantic_instance.deadline,
    )


def get_task_or_404_if_not_exist(instance: TaskEntity | None) -> TaskEntity:
    """Return the entity or raise 404 if it is None."""
    if instance is None:
        logger.info(f"Попытка доступа к несуществующей сущности")
        raise HTTPException(status_code=404, detail=task_not_found_response)
    return instance


@tasks_router.get(
    "/",
    summary="Вывести список всех задач пользователя",
    description="Выводит json со списком всех задач, которые есть в БД",
    response_description="Данные задач",
)
async def list_tasks() -> list[TaskEntity]:
    return await tasks_service.get_all_tasks()


@tasks_router.get(
    "/{task_id}",
    summary="Вывести задачу по id",
    description="Выводит все данные задачи, находя ее по id: int",
    response_description="Данные задачи",
)
async def get_task(task_id: int) -> TaskEntity:
    task: TaskEntity | None = await tasks_service.get_task_by_id(task_id)
    return get_task_or_404_if_not_exist(task)


@tasks_router.post(
    "/",
    summary="Создать задачу",
    description="Позволяет создать задачу в БД",
    response_description="Возвращает данные созданной задачи",
    status_code=status.HTTP_201_CREATED,
)
async def create_task(task_pydantic_instance: TaskCreate):
    try:
        task = map_task_pydantic_to_dto(task_pydantic_instance)
        return await tasks_service.create_task(task)
    except DeadlineInPastError as e:
        raise HTTPException(status_code=400, detail=str(e))


@tasks_router.delete(
    "/{task_id}",
    summary="Удалить задачу по id",
    description="Удаляет задачу из БД по ее id: int",
    response_description="Данные удаленной задачи",
    responses={200: task_delete_response, 404: task_not_found_response},
)
async def delete_task(task_id: int) -> TaskEntity:
    task: TaskEntity | None = await tasks_service.delete_task_by_id(task_id)
    return get_task_or_404_if_not_exist(task)


@tasks_router.patch(
    "/rearrange/{task_id}",
    summary="Изменить время дедлайна задачи",
)
async def change_task_deadline(
    task_id: int, new_deadline: ChangeDeadline
) -> TaskEntity:
    try:
        response: TaskEntity | None = await tasks_service.change_task_deadline(
            task_id, new_deadline.deadline
        )
        return get_task_or_404_if_not_exist(response)
    except DeadlineInPastError as e:
        raise HTTPException(status_code=400, detail=str(e))


@tasks_router.patch("/mark_completed/{task_id}", summary="Отметить таску выполненной")
async def mark_task_completed(task_id: int) -> TaskEntity:
    response: TaskEntity | None = await tasks_service.mark_task_completed(task_id)  # type: ignore
    return get_task_or_404_if_not_exist(response)
