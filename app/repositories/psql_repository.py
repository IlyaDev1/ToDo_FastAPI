from .base_repository import BaseRepository
from typing import Type, List
from sqlalchemy.orm import Session
from . import ModelType


class PsqlRepository(BaseRepository):
    def __init__(self, db: Session, model: Type[ModelType]) -> None:
        self.db = db
        self.model = model

    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()
