from datetime import datetime

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str
    description: str | None
    deadline: datetime | None


class ChangeDeadline(BaseModel):
    deadline: datetime = Field(..., description="Дата и время нового дедлайна")
