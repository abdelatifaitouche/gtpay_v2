from fastapi import FastAPI, Depends, Request
from src.api.router import api
from src.core.exceptions import AppException
from src.core.config import settings
from src.api.exception_handlers import register_exception_handlers
from src.api.middlewares.request_logging import request_logging_middleware
from src.core.logging import setup_logging


def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(version="v1", title="gtpay api")

    register_exception_handlers(app)

    app.middleware("http")(request_logging_middleware)

    app.include_router(api)

    return app


app: FastAPI = create_app()
