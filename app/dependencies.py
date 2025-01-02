from sqlalchemy.orm import Session
from app.database import SessionLocal


def get_db() -> Session:
    """
    Зависимость для получения объекта сессии базы данных.
    Управляет открытием и закрытием сессии.
    """
    db = SessionLocal()
    try:
        yield db  # Передаем сессию в вызывающую функцию
    finally:
        db.close()  # Закрываем сессию после завершения работы
