from app.repositories.task.impl.task_psql_repository import TaskPSQLRepository
from app.models.task_model import TaskModel
from app.core.dependencies import get_db
from fastapi import Depends


class TaskService:
    def __init__(self):
        self.task_psql_repo: TaskPSQLRepository = TaskPSQLRepository(Depends(get_db), TaskModel)

    def get_all_tasks(self):
        return self.task_psql_repo.get_all()
