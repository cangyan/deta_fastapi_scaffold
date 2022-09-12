from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    PROJECT_KEY: str
    LOG_FILE: str = "/tmp/app.log"
    LOG_LEVEL: str = "debug"
    TIMEOUT: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
