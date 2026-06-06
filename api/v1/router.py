from fastapi import APIRouter

from api.v1.routers import health, workflows

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(workflows.router, tags=["workflows"])
