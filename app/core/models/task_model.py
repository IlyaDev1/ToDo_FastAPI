from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, func
from app.core.models.base import Base
from datetime import datetime


class TaskModel(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(60), index=True, nullable=False)
    description = Column(Text, nullable=True, default=None)
    is_completed = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deadline = Column(DateTime, nullable=True, default=None)
