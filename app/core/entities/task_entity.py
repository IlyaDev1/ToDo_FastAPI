from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskEntity:
    id: int | None
    title: str
    description: str | None
    is_completed: bool | None
    created_at: datetime | None
    deadline: datetime | None
