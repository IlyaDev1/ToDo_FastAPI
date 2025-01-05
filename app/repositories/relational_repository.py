from abc import ABC, abstractmethod
from . import ModelType
from typing import Generic, Type
from sqlalchemy.orm import Session


class RelationalRepository(ABC, Generic[ModelType]):
    @abstractmethod
    def __init__(self):
        ...
