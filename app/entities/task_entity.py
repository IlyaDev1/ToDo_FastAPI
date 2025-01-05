import datetime
from dataclasses import dataclass


@dataclass
class TaskEntity:
    id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime.datetime
    deadline: datetime.datetime
