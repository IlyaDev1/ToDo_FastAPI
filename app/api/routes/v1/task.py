from fastapi import APIRouter
from fastapi.responses import JSONResponse
from inject import is_configured

from app.api.schemas.task import ChangeDeadline, TaskCreate
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


@tasks_router.get("/", summary="Вывести список всех задач пользователя")
async def list_tasks():
    return await tasks_service.get_all_tasks()


@tasks_router.get("/{task_id}", summary="Вывести задачу по id")
async def get_task(task_id: int):
    task = await tasks_service.get_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task


@tasks_router.post("/", summary="Создать задачу")
async def create_task(task_pydantic_instance: TaskCreate):
    task = map_task_pydantic_to_dto(task_pydantic_instance)
    return await tasks_service.create_task(task)


@tasks_router.delete("/{task_id}", summary="Удалить задачу по id")
async def delete_task(task_id: int):
    task = await tasks_service.delete_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task


@tasks_router.patch("/rearrange/{task_id}", summary="Изменить время дедлайна задачи")
async def change_task_deadline(task_id: int, new_deadline: ChangeDeadline):
    response = await tasks_service.change_task_deadline(task_id, new_deadline.deadline)
    if response is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return response
