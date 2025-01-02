from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    DATABASE_URL = "postgresql://user:password@localhost/dbname"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
