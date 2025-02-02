from fastapi import APIRouter, HTTPException
from app.core.service.db_service import TaskService
from inject import is_configured


tasks_router = APIRouter()

if is_configured():
    tasks_service = TaskService()


@tasks_router.get("/")
def list_tasks():
    return tasks_service.get_all_tasks()


@tasks_router.get('/{task_id}')
def get_task(task_id: int):
    task = tasks_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=204, detail='task with this id is not exists')
