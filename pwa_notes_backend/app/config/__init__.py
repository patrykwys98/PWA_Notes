from .common import CommonSettings
from .database import DatabaseSettings
from .server import ServerSettings


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    class Config:
        env_file = '././.env'
    pass


settings = Settings()