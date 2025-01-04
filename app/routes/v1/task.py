from fastapi import APIRouter
from app.service.db_service import TaskService


tasks_router = APIRouter()
tasks_service = TaskService()


@tasks_router.get("/")
def list_tasks():
    return tasks_service.get_all_tasks()
