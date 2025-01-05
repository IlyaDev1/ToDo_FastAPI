from contextlib import contextmanager

from sqlalchemy.orm import Session
from .database import database
from ..models.todo import Task
from ..repositories.task.impl.task_psql_repository import TaskPSQLRepository
from ..repositories.task.task_repository import TaskRepository


@contextmanager
def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.commit()
        db.close()


def production_config(binder):
    with get_db() as db:
    # db = next(get_db())
        binder.bind(TaskRepository, TaskPSQLRepository(db, Task))
