from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from app.api.schemas.constants import MAX_DESCRIPTION_LENGTH, MAX_TITLE_LENGTH


class TaskCreate(BaseModel):
    title: str = Field(
        ..., max_length=MAX_TITLE_LENGTH, min_length=1, description="Оглавление задачи"
    )
    description: str | None = Field(
        None, max_length=MAX_DESCRIPTION_LENGTH, description="Подробное описание задачи"
    )
    deadline: datetime | None = Field(
        None, description="Время, до которого нужно сделать задачу"
    )

    @field_validator("deadline")
    @classmethod
    def deadline_must_be_in_future(cls, value: datetime):
        if value is not None and value < datetime.now():
            raise ValueError("Deadline must be in future")
        return value


class ChangeDeadline(BaseModel):
    deadline: datetime = Field(..., description="Дата и время нового дедлайна")
