from abc import ABC, abstractmethod
from typing import Type, Generic, List
from . import ModelType


class BaseRepository(ABC, Generic[ModelType]):
    @abstractmethod
    def __init__(self) -> None:  # Я хочу создавать объект репы
        ...

    @abstractmethod
    def get_all(self) -> List[ModelType]:  # Пока что просто получаю все таски
        ...
