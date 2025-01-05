import inject
from fastapi import FastAPI

from app.core.dependencies import production_config

inject.configure(production_config)

from app.routes.v1 import api_router


app = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="API for managing tasks and users"
)



app.include_router(api_router, prefix="/api/v1")
