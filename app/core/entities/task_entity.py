from dataclasses import dataclass
from datetime import datetime


@dataclass
class TaskEntity:
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    deadline: datetime
