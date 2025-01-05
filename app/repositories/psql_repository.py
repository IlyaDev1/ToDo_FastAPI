from .relational_repository import RelationalRepository
from . import ModelType
from sqlalchemy.orm import Session
from typing import Type


class PsqlRepository(RelationalRepository):
    def __init__(self, db: Session, model: Type[ModelType]) -> None:
        self.db = db
        self.model = model
