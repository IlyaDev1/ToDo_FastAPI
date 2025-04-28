from datetime import datetime

from pydantic import BaseModel, Field, field_validator


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

    @field_validator("deadline")
    @classmethod
    def deadline_must_be_in_future(cls, value: datetime):
        if value is not None:
            value = value.replace(tzinfo=None)
            if value < datetime.now():
                raise ValueError("Deadline must be in future")
        return value


class ChangeDeadline(BaseModel):
    deadline: datetime = Field(..., description="Дата и время нового дедлайна")
