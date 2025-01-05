import inject

from app.repositories.psql_repository import PsqlRepository
from app.models.todo import Task
from app.core.dependencies import get_db
from fastapi import Depends

from app.repositories.task.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.task_repo: TaskRepository = inject.instance(TaskRepository)
        # self.psql_repo: PsqlRepository = PsqlRepository(Depends(get_db), Task)

    def get_all_tasks(self):
        return self.task_repo.get_all()
