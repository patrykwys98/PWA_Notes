from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str