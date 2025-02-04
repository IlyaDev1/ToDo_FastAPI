from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.service.db_service import TaskService
from inject import is_configured
from app.api.schemas.task import TaskCreate
from app.core.entities.task_entity import TaskEntity


tasks_router = APIRouter()

if is_configured():
    tasks_service = TaskService()


@tasks_router.get("/")
def list_tasks():
    return tasks_service.get_all_tasks()


@tasks_router.get('/{task_id}')
def get_task(task_id: int):
    task = tasks_service.get_task_by_id(task_id)
    if task is None:
        return JSONResponse(content={'msg': 'task with this ID does not exist'}, status_code=404)
    return task


@tasks_router.post('/')
def create_task(task_data: TaskCreate):
    task_entity = TaskEntity(
        id=None,
        title=task_data.title,
        description=task_data.description,
        is_completed=None,
        created_at=None,
        deadline=task_data.deadline,
    )
    created_task = tasks_service.create_task(task_entity)
    return created_task
