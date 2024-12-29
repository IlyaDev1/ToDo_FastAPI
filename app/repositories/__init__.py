from typing import TypeVar
from app.models.base import Base


ModelType = TypeVar("ModelType", bound=Base)


__all__ = ["ModelType"]
