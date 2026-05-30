from sqlalchemy.ext.asyncio import AsyncSession


class FileRepository:
    model: str = ""

    def __init__(self, db: AsyncSession):
        self.db: AsyncSession = db

    async def bulk_insert(self):
        return

    async def get_by_id(self):
        return

    async def update(self):
        return

    async def delete(self):
        return

    async def save(self):
        return

    async def list(self):
        return

    def __apply_pagination(self):
        return

    def __apply_filters(self):
        return
