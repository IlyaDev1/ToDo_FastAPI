from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = getenv("APP_NAME", "Calendar")
    API_V1_STR: str = getenv("API_V1_STR", "/api/v1")
    DATABASE_URL: str = getenv(
        "ASYNC_DATABASE_URL", "postgresql+async://postgres:postgres@db:5432/postgres"
    )
    DESCRIPTION: str = getenv("DESCRIPTION", "API for managing tasks and users")
    DEBUG: str = getenv("DEBUG", "false")
    APP_CONTAINER_PORT: int = int(getenv("APP_CONTAINER_PORT", "8085"))
    APP_HOST_PORT: int = int(getenv("APP_HOST_PORT", "8080"))


settings = Settings()
