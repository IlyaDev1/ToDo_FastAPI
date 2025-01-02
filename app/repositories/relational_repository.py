from .base_repository import BaseRepository
from . import ModelType
from typing import Generic, Type
from sqlalchemy.orm import Session


class RelationalRepository(BaseRepository, Generic[ModelType]):
    def __init__(self, db: Session, model: Type[ModelType]) -> None:
        self.db = db
        self.model = model

    def get_all(self) -> list[ModelType]:
        ...
