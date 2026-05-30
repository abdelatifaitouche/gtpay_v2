from abc import ABC, abstractmethod


class FileStorage(ABC):
    async def upload(self, key: str, data: bytes, content_type: str) -> str:
        pass

    async def download(self, key: str) -> bytes:
        pass

    async def delete(self, key: str) -> None:
        pass

    async def get_presigned_url(self, key: str, expires_in: int = 3600) -> str:
        pass
