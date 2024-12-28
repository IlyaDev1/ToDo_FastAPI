from typing import Generic, Type, TypeVar, Optional, List
from sqlalchemy.orm import Session
from app.models.base import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """Базовый репозиторий."""
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        """Получить объект по ID."""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[ModelType]:
        """Получить все объекты."""
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: dict) -> ModelType:
        """Создать объект."""
        obj = self.model(**obj_in)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, db_obj: ModelType, obj_in: dict) -> ModelType:
        """Обновить объект."""
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> Optional[ModelType]:
        """Удалить объект по ID."""
        obj = db.query(self.model).filter(self.model.id == id).first()
        if obj:
            db.delete(obj)
            db.commit()
        return obj
