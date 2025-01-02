from sqlalchemy.orm import Session
from app.database import Database


def get_db() -> Session:
    """
    Зависимость для получения объекта сессии базы данных.
    Управляет открытием и закрытием сессии.
    """
    db = Database.SessionLocal()
    try:
        yield db  # Передаем сессию в вызывающую функцию
    finally:
        db.close()  # Закрываем сессию после завершения работы
