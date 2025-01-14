from app.entities.task_entity.task_entity import TaskEntity
from app.repositories.specific_dms.psql_repository import PsqlRepository
from app.repositories.task.task_repository import TaskRepository


class TaskPSQLRepository(TaskRepository, PsqlRepository):
    def get_all(self) -> list[TaskEntity]:
        objs: list = self.session_instance.query(self.model_instance).all()
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
