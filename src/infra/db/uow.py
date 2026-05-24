from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.session import SessionLocal


class UnitOfWork:
    """
    UNIT OF WORK :
        single transaction control
    """

    def __init__(self):
        self.session: AsyncSession | None = None

    async def __aenter__(self):
        self.session = SessionLocal()
        return self.session

    async def __aexit__(self, exc_type, exc, tb):
        try:
            if exc_type:
                await self.session.rollback()
            else:
                await self.session.commit()
        finally:
            await self.session.close()
