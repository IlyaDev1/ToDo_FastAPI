class Settings:
    APP_NAME: str = "Task Management API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5433/postgres"
    DESCRIPTION: str = "API for managing tasks and users"
    DEBUG: bool = True

    SECRET_KEY: str = "super-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # class Config:  пока не использую переменные окружения
    #     env_file = ".env"


settings = Settings()
