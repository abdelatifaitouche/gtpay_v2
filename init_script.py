from src.core.logging import setup_logging

setup_logging()


import asyncio
from src.infra.db.seeds.seed_permissions import seed_permissions
from src.infra.db.seeds.seed_roles import seed_roles
from src.infra.db.seeds.seed_role_permissions import seed_role_permissions
from src.infra.db.session import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
import logging

logger = logging.getLogger(__name__)


async def run(session: AsyncSession):
    logger.info("Starting seeding process...")

    logger.info("Inserting permissions...")
    await seed_permissions(session)
    logger.info("Permissions inserted ..... OK")

    logger.info("Inserting roles...")
    await seed_roles(session)
    logger.info("Roles inserted ..... OK")

    logger.info("Linking role permissions...")
    await seed_role_permissions(session)
    logger.info("Role permissions linked ...... OK")

    logger.info("Seeding completed successfully ✓")


async def main():
    logger.info("Initializing database session...")
    async with SessionLocal() as session:
        try:
            await run(session)
            await session.commit()
            logger.info("Transaction committed ........ OK")
        except Exception as e:
            await session.rollback()
            logger.exception(f"Seeding failed, transaction rolled back: {e}")
            raise
        finally:
            await session.close()
            logger.info("Session closed ....")


if __name__ == "__main__":
    asyncio.run(main())
