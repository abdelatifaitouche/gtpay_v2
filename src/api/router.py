from fastapi import APIRouter
from src.features.auth.routes import router as auth_router


api = APIRouter(prefix="/api/v1")


api.include_router(auth_router)
