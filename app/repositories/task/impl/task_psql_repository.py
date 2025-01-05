from app.entities.task_entity import TaskEntity
from app.repositories.psql_repository import PsqlRepository
from app.repositories.task.task_repository import TaskRepository


class TaskPSQLRepository(TaskRepository, PsqlRepository):
    def get_all(self) -> list[TaskEntity]:
        objs: list = self.db.query(self.model).all()  # TODO: type hint
        return list(map(
            lambda obj: TaskEntity(
                id=obj.id,
                title=obj.title,
                description=obj.description,
                is_completed=obj.is_completed,
                created_at=obj.created_at,
                deadline=obj.deadline,
            ),
            objs
        ))
