from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    SSH_HOST: str | None = None
    SSH_PORT: int | None = 22
    SSH_USERNAME: str | None = None
    SSH_PRIVATE_KEY_PATH: str | None = None
    REMOTE_DB_HOST: str | None = None
    REMOTE_DB_PORT: int | None = 5432

    class Config:
        env_file = ".env"

settings = Settings()