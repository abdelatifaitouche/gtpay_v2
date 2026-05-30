from functools import lru_cache
from minio import Minio
from src.core.config import settings


def _is_valid(value: str) -> bool:
    return isinstance(value, str) and value.strip() != ""


@lru_cache
def get_storage_client():

    endpoint: str = settings.MINIO_ENDPOINT
    access_key: str = settings.MINIO_ACCESS_KEY
    secret_key: str = settings.MINIO_SECRET_KEY

    if not all(
        [
            _is_valid(endpoint),
            _is_valid(access_key),
            _is_valid(secret_key),
        ]
    ):
        raise ValueError("Invalid MinIO Configuration")

    return Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=settings.MINIO_IS_SECURE,
    )
