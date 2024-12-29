from abc import ABC, abstractmethod
from typing import Type, Generic
from . import ModelType


class BaseRepository(ABC, Generic[ModelType]):
    @abstractmethod
    def __init__(self):  # Я хочу создавать объект репы
        ...

    @abstractmethod
    def get_all(self, model: Type[ModelType]):  # Пока что просто получаю все таски
        ...
