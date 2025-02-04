from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None


class TaskCreate(TaskBase):
    ...


class TaskUpdate(TaskBase):
    ...


class TaskDelete(BaseModel):
    id: int
