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


@tasks_router.get("/")
def list_tasks():
    return tasks_service.get_all_tasks()


@tasks_router.get("/{task_id}")
def get_task(task_id: int):
    task = tasks_service.get_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task


@tasks_router.post("/")
def create_task(task_pydantic_instance: TaskCreate):
    task = map_task_pydantic_to_dto(task_pydantic_instance)
    return tasks_service.create_task(task)


@tasks_router.delete("/{task_id}")
def delete_task(task_id: int):
    task = tasks_service.delete_task_by_id(task_id)
    if task is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return task


@tasks_router.patch(
    "/rearrange/{task_id}",
    summary="Изменить время дедлайна задачи",
)
def change_task_deadline(task_id: int, timing: ChangeDeadline):
    new_timing = timing.deadline
    response = tasks_service.change_task_deadline(task_id, new_timing)
    if response is None:
        logger.warning(f"Попытка доступа к несуществующей задаче ID {task_id}")
        return JSONResponse(
            content={"msg": "task with this ID does not exist"}, status_code=404
        )
    return response
