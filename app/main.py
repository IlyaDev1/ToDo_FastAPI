from fastapi import FastAPI
from inject import configure, is_configured
from uvicorn import run

from app.core.binding import production_config
from app.core.config import settings

if not is_configured():
    configure(production_config)

from app.api.routes.v1 import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_V1_STR,
    description=settings.DESCRIPTION,
)

app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    run("main:app", reload=False, host="0.0.0.0", port=settings.APP_CONTAINER_PORT)
