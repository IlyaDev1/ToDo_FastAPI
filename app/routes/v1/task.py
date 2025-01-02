from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repositories.psql_repository import PsqlRepository
from app.models.todo import Task
from app.dependencies import get_db


tasks_router = APIRouter()


def get_task_repository(db: Session = Depends(get_db)) -> PsqlRepository:
    return PsqlRepository(db, Task)


@tasks_router.get("/")
async def list_tasks(repo: PsqlRepository = Depends(get_task_repository)):
    return repo.get_all()
