from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


class Database:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


database = Database()
