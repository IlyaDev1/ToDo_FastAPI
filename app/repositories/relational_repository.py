from abc import ABC, abstractmethod
from . import ModelType, SessionType
from typing import Generic, Type


class RelationalRepository(ABC, Generic[ModelType]):
    @abstractmethod
    def __init__(self, session_instance: SessionType, model: Type[ModelType]) -> None:
        ...
