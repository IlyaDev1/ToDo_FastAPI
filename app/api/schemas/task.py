from datetime import datetime

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., description="Оглавление задачи")
    description: str | None = Field(None, description="Подробное описание задачи")
    deadline: datetime | None = Field(
        None, description="Время, до которого нужно сделать задачу"
    )


class ChangeDeadline(BaseModel):
    deadline: datetime = Field(..., description="Дата и время нового дедлайна")
