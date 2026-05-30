from fastapi import APIRouter, Depends
from src.features.auth.dependencies import get_auth_service
from src.features.auth.services.auth_service import AuthService

router = APIRouter(prefix="/auth")


@router.post("/register/")
async def register_user(service: AuthService = Depends(get_auth_service)):
    return "Register User"
