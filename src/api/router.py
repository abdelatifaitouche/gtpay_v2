from fastapi import APIRouter
from src.features.auth.routes import router as auth_router
from src.features.tenant.routes import router as tenant_router

api = APIRouter(prefix="/api/v1")


api.include_router(auth_router)
api.include_router(tenant_router)
