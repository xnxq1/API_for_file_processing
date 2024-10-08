from typing import Literal

from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    MODE: Literal['DEV', 'TEST']

    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SECRETKEY: str
    ALGORITHM: str

    REDIS_HOST: str
    REDIS_PORT: int

    TEST_DB_HOST: str
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}/{self.TEST_DB_NAME}"


settings = Settings()
