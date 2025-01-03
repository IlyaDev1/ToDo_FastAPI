from sqlalchemy.orm import Session
from .database import Database


def get_db() -> Session:
    db = Database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
