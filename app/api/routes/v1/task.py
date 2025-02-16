from fastapi import APIRouter
from fastapi.responses import JSONResponse
from inject import is_configured

from app.api.schemas.task import TaskCreate
from app.core.dtos.task_dto import TaskDTO
from app.core.service.db_service import TaskService
from logger import logger

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


@tasks_router.get(
    "/",
    summary="Вывести список всех задач пользователя",
    description="Выводит json со списком всех задач, которые есть в БД",
    response_description="Данные задач",
)
def list_tasks():
    return tasks_service.get_all_tasks()


@tasks_router.get(
    "/{task_id}",
    summary="Вывести задачу по id",
    description="Выводит все данные задачи, находя ее по id: int",
    response_description="Данные задачи",
)
def get_task(task_id: int):
    task = tasks_service.get_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task


@tasks_router.post(
    "/",
    summary="Создать задачу",
    description="Позволяет создать задачу в БД",
    response_description="Возвращает данные созданной задачи",
)
def create_task(task_pydantic_instance: TaskCreate):
    task = map_task_pydantic_to_dto(task_pydantic_instance)
    return tasks_service.create_task(task)


@tasks_router.delete(
    "/{task_id}",
    summary="Удалить задачу по id",
    description="Удаляет задачу из БД по ее id: int",
    response_description="Данные удаленной задачи",
    responses={
        200: {
            "description": "Задача успешно удалена",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "title",
                        "description": "description",
                        "deadline": "2023-12-31T23:59:59",
                    }
                }
            },
        },
        404: {
            "description": "Задача с таким id не существует",
            "content": {
                "application/json": {
                    "example": {"msg": "task with this ID does not exist"}
                }
            },
        },
    },
)
def delete_task(task_id: int):
    task = tasks_service.delete_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task
