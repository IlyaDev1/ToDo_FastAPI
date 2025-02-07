from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    id: int | None
    title: str
    description: str | None = None
    is_completed: bool = False
    deadline: datetime | None = None


class TaskCreate(TaskBase):
    ...


class TaskUpdate(TaskBase):
    ...


class TaskDelete(BaseModel):
    id: int
