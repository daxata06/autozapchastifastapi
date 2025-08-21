from pydantic.v1 import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # for tronpy
    PRIVATE_KEY = "8888888888888888888888888888888888888888888888888888888888888888"


@lru_cache
def get_settings():
    return Settings()
