from fastapi import FastAPI
from app.routes.v1 import api_router


app = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="API for managing tasks and users"
)


app.include_router(api_router, prefix="/api/v1")
