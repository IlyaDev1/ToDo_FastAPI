from .base_repository import BaseRepository
from typing import Type, List
from sqlalchemy.orm import Session
from . import ModelType


class PsqlRepository(BaseRepository):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
