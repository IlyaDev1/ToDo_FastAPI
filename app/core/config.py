from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Settings:
    APP_NAME: str = getenv('APP_NAME')
    API_V1_STR: str = getenv('API_V1_STR')
    DATABASE_URL: str = getenv('DATABASE_URL')
    DESCRIPTION: str = getenv('DESCRIPTION')
    DEBUG: bool = getenv('DEBUG').lower() == 'true'
    APP_CONTAINER_PORT: int = int(getenv('APP_CONTAINER_PORT'))


settings = Settings()
