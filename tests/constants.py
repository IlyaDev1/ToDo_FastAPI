from datetime import datetime, timedelta

from app.core.dtos.task_dto import TaskDTO

CURRENT_TIMESTAMP: datetime = datetime.now()

TASK_URL = "/api/v1/task/"  # url to task endpoint
CHANGE_DEADLINE_URL = TASK_URL + "rearrange/"  # url to change deadline endpoint

TASK_DTO_INSTANCE = TaskDTO(
    title="title",
    description="description",
    deadline=CURRENT_TIMESTAMP + timedelta(days=1),
    is_completed=False,
    created_at=CURRENT_TIMESTAMP,
)
