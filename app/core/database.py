from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, echo=True)


AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, autocommit=False, autoflush=False
)
