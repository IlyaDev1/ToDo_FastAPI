from abc import ABC, abstractmethod
from . import ModelType


class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[ModelType]:  # Пока что просто получаю все таски
        ...
