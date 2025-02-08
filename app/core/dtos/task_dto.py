from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskDTO:
    id: int | None
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime | None
    deadline: datetime | None
