from sqlalchemy.orm import Session
from .database import database
from contextlib import contextmanager
from app.repositories.task_repository import TaskRepository
from app.repositories.impl.task_psql_repository import TaskPSQLRepository


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
        binder.bind(TaskRepository, TaskPSQLRepository(db))
