from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from app.models.base import Base
from datetime import datetime


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(60), index=True, nullable=False)
    description = Column(Text, nullable=True, default=None)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    deadline = Column(DateTime, nullable=True, default=None)
