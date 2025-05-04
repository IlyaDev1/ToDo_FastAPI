from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

sync_engine = create_engine(settings.SYNC_DATABASE_URL, echo=False)
