from src.core.ports.storage import FileStorage
from datetime import timedelta
from minio import Minio


class MinIOStorage(FileStorage):
    def __init__(self, client: Minio, bucket: str):
        self._client: Minio = client
        self.bucket = bucket

    async def get_presigned_url(self, key: str, expires_in: int = 3600) -> str:
        """
        IMPORTANT:
            - this method is used only to generate presigned urls for the client
            to upload to the quarantine Bucket Only
        """

        return self._client.presigned_put_object(
            self.bucket, key, expires=timedelta(hours=expires_in)
        )
