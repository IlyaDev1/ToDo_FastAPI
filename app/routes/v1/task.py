from fastapi import APIRouter
from app.service.db_service import TaskService
from inject import is_configured


tasks_router = APIRouter()

if is_configured():
    tasks_service = TaskService()


@tasks_router.get("/")
def list_tasks():
    return tasks_service.get_all_tasks()
