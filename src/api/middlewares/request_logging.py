import time
import logging
from fastapi import Request

logger = logging.getLogger("api.request")


async def request_logging_middleware(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        "request",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration * 1000, 2),
        },
    )

    return response
