from functools import lru_cache
from fastapi import FastAPI, Depends
from minio import Minio
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from pydantic import BaseModel
from src.api.router import api

load_dotenv()


app = FastAPI(version="v1", title="gtpay api")

app.include_router(api)


@app.get("/health")
def routes():
    return "Hello GTPAY"


@lru_cache
def get_storage_client():
    endpoint: str | None = os.getenv("MINIO_ENDPOINT")
    access_key: str | None = os.getenv("MINIO_ACCESS_KEY")
    secret_key: str | None = os.getenv("MINIO_SECRET_KEY")

    if not endpoint or not access_key or not secret_key:
        raise ValueError("Error while init minio")

    return Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=False,
    )


@dataclass
class Url:
    url: str


class UrlRead(BaseModel):
    url: str

    model_config = {"from_attributes": True}


from datetime import timedelta


class StorageService:
    def __init__(self, client: Minio):
        self._client = client

    def create_bucket(self):
        bucket_name: str = "test-bucket"

        if not self._client.bucket_exists(bucket_name):
            self._client.make_bucket(bucket_name)
        return bucket_name

    def get_upload_url(self) -> Url:
        url: str = self._client.presigned_put_object(
            "test-bucket", "untrusted_file.txt", expires=timedelta(minutes=5)
        )

        if not url:
            raise Exception("Error while generating preseinged url")

        return Url(url=url)


def get_service(client: Minio = Depends(get_storage_client)):
    return StorageService(client)


@app.post("/create_bucket")
def create_bucket(service: StorageService = Depends(get_service)):
    bucket = service.create_bucket()
    return bucket


@app.get("/upload")
def upload_file(service: StorageService = Depends(get_service)):

    generated_url: Url = service.get_upload_url()

    return UrlRead.model_validate(generated_url)
