from contextlib import contextmanager

from sqlalchemy.orm import Session

from .database import database


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
