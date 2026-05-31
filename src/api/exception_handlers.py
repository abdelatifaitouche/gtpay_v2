from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.core.config import settings
from src.core.exceptions import AppException, ValidationError
from src.core.logging import get_logger

logger = get_logger("api")


def register_exception_handlers(app: FastAPI):

    # -------------------------
    # 1. Your custom exceptions
    # -------------------------
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):

        logger.error(
            "Application exception",
            extra={
                "path": str(request.url),
                "type": type(exc).__name__,
                "status_code": exc.status_code,
                "message": exc.message,
            },
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "sucess": False,
                "message": exc.message,
                "details": exc.details if settings.DEBUG else None,
            },
        )

    # -----------------------------------
    # 2. FastAPI / Pydantic validation
    # -----------------------------------
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):

        logger.warning(
            "Invalid request payload",
            extra={
                "path": str(request.url),
                "method": request.method,
                "status_code": 422,
                "errors": exc.errors(),
            },
        )

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation error",
                "details": exc.errors() if settings.DEBUG else None,
            },
        )
