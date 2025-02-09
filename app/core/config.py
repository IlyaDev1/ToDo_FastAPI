from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME: str | None = getenv('APP_NAME')
    API_V1_STR: str | None = getenv('API_V1_STR')
    DATABASE_URL: str | None = getenv('DATABASE_URL')
    DESCRIPTION: str | None = getenv('DESCRIPTION')
    DEBUG: bool | None = getenv('DEBUG').lower() == 'false'
    APP_CONTAINER_PORT: int | None = int(getenv('APP_CONTAINER_PORT'))


settings = Settings()
