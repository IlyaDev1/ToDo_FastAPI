from .relational_repository import RelationalRepository
from . import ModelType


class PsqlRepository(RelationalRepository):
    def get_all(self) -> list[ModelType]:
        return self.db.query(self.model).all()
