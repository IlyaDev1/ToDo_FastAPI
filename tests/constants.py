from datetime import datetime, timedelta

from app.core.dtos.task_dto import TaskDTO

current_timestamp = datetime.now()

TASK_URL = "/api/v1/task/"  # url to task endpoint

TASK_DTO_INSTANCE = TaskDTO(
    title="title",
    description="description",
    deadline=current_timestamp + timedelta(days=1),
    is_completed=False,
    created_at=current_timestamp,
)
