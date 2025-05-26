from datetime import datetime

from pydantic import BaseModel, Field

from app.api.schemas.constants import (
    MAX_DESCRIPTION_LENGTH,
    MAX_TITLE_LENGTH,
    MIN_TITLE_LENGTH,
)


class ChangeDeadline(BaseModel):
    deadline: datetime | None = Field(None, description="Дедлайн задачи")


class TaskCreate(ChangeDeadline):
    title: str = Field(
        ...,
        max_length=MAX_TITLE_LENGTH,
        min_length=MIN_TITLE_LENGTH,
        description="Оглавление задачи",
    )
    description: str | None = Field(
        None, max_length=MAX_DESCRIPTION_LENGTH, description="Подробное описание задачи"
    )
    deadline: datetime | None = Field(None, description="Дедлайн задачи")
