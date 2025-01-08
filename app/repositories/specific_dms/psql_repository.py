from app.repositories.relational_repository import RelationalRepository
from sqlalchemy.orm import Session
from app.models.task_model import TaskModel


class PsqlRepository(RelationalRepository):
    def __init__(self, session_instance: Session, model_instance: TaskModel) -> None:
        self.session_instance = session_instance
        self.model_instance = model_instance
