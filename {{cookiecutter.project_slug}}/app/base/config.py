from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    LOG_FILE: str
    LOG_LEVEL: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
