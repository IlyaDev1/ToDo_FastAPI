from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TaskEntity:
    id: Optional[int]
    title: str
    description: Optional[str]
    is_completed: Optional[bool]
    created_at: Optional[datetime]
    deadline: Optional[datetime]
