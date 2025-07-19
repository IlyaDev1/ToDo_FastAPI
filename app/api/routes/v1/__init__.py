"""
В __init__ предлагается объединять все роутеры, чтобы получить итоговый роутер api_router
"""

from fastapi import APIRouter

from .task import tasks_router

api_router = APIRouter()
api_router.include_router(tasks_router, prefix="/task", tags=["Task"])
