from sqlalchemy.orm import Session
from .database import database
from contextlib import contextmanager


@contextmanager
def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
