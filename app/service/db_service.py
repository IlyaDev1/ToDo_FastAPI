from app.repositories.psql_repository import PsqlRepository
from app.models.todo import Task
from app.core.dependencies import get_db
from fastapi import Depends


class TaskService:
    def __init__(self):
        self.psql_repo: PsqlRepository = PsqlRepository(Depends(get_db), Task)

    def get_all_tasks(self):
        return self.psql_repo.get_all()
