from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.api.schemas.constants import MAX_DESCRIPTION_LENGTH, MAX_TITLE_LENGTH


class ChangeDeadline(BaseModel):
    deadline: datetime | None = Field(None, description="Дедлайн задачи")
    @field_validator("deadline")
    @classmethod
    def deadline_must_be_in_future(cls, value: datetime):
        if value is not None:
            value = value.replace(tzinfo=None)
            if value < datetime.now():
                raise ValueError("Deadline must be in future")
        return value


class TaskCreate(ChangeDeadline):
    title: str = Field(
        ..., max_length=MAX_TITLE_LENGTH, min_length=1, description="Оглавление задачи"
    )
    description: str | None = Field(
        None, max_length=MAX_DESCRIPTION_LENGTH, description="Подробное описание задачи"
    )
