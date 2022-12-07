from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL.replace(
    'postgres://', "postgresql+psycopg2://")
engine = create_engine(
    DATABASE_URL
)
engine.execute(
    text("CREATE EXTENSION IF NOT EXISTS ltree;").execution_options(autocommit=True))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
