from pydantic import BaseSettings


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000