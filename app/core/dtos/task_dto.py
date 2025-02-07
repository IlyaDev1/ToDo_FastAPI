from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskDTO:
    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime
    deadline: datetime | None
