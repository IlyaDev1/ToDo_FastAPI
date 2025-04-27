from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class TaskDTO:
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime | None
    deadline: datetime | None

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "deadline": self.deadline.isoformat() if self.deadline else None,
        }
