from datetime import datetime

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(
        ..., max_length=60, min_length=1, description="Оглавление задачи"
    )
    description: str | None = Field(
        None, max_length=2000, description="Подробное описание задачи"
    )
    deadline: datetime | None = Field(
        None, description="Время, до которого нужно сделать задачу"
    )


class ChangeDeadline(BaseModel):
    deadline: datetime = Field(..., description="Дата и время нового дедлайна")
