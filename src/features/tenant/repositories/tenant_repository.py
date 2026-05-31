import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import (
    NoResultFound,
    IntegrityError,
    OperationalError,
    ProgrammingError,
    DataError,
    InterfaceError,
    SQLAlchemyError,
)
from src.core.exceptions import NotFoundError, DatabaseError, ValidationError
from sqlalchemy import select
from uuid import UUID
from src.features.tenant.domaine.tenant import (
    Tenant as TenantEntity,
    CreateTenant as CreateTenantEntity,
    TenantUpdate as TenantUpdateDTO,
)
from src.features.tenant.models.tenant import Tenant as TenantDB


logger = logging.getLogger("tenant.repository")


class TenantRepository:
    model = TenantDB

    def __init__(self, db: AsyncSession):
        self.db: AsyncSession = db

    def translate_db_error(self, e: Exception):
        """
        This should be in the base Repository
        """
        match e:
            case IntegrityError():
                logger.exception("Integrity error")
                raise ValidationError("Constraint Violation") from e
            case OperationalError():
                logger.exception("Operational error")
                raise DatabaseError("Database Unavailable") from e
            case ProgrammingError():
                logger.exception("Programming error")
                raise DatabaseError("Query error / schema error") from e
            case DataError():
                logger.exception("Data error")
                raise ValidationError("Invalid Data format") from e
            case InterfaceError():
                logger.exception("Interface error")
                raise DatabaseError("Db Session Error") from e
            case _:
                logger.exception("Programming error")
                raise DatabaseError("Unkown database Error") from e

    def to_orm(self, tenant: TenantEntity) -> TenantDB:
        return TenantDB(
            id=tenant.id,
            status=tenant.status,
            type=tenant.type,
            name=tenant.name,
            is_active=tenant.is_active,
        )

    def to_domain(self, orm: TenantDB) -> TenantEntity:
        return TenantEntity(
            id=orm.id,
            name=orm.name,
            type=orm.type,
            status=orm.status,
            is_active=orm.is_active,
        )

    async def save(self, tenant: TenantEntity) -> TenantEntity:
        orm = self.to_orm(tenant)
        orm = await self.db.merge(orm)
        await self.db.flush()
        await self.db.refresh(orm)
        return self.to_domain(orm)

    async def list(self) -> list[TenantEntity]:
        stmt = select(self.model)
        results = await self.db.execute(stmt)
        data = results.scalars().all()
        return [self.to_domain(obj) for obj in data]

    async def get_by_id(self, tenant_id: UUID) -> TenantEntity:
        stmt = select(self.model).where(self.model.id == tenant_id)
        try:
            result = await self.db.execute(stmt)
            data = result.scalar_one_or_none()

            if not data:
                raise NotFoundError("Entity Not Found", details={"id": str(tenant_id)})

            return self.to_domain(data)
        except SQLAlchemyError as e:
            logger.exception(
                "DB error in get_by_id",
                extra={
                    "model": self.model.__name__,
                    "id": str(tenant_id),
                },
            )
            self.translate_db_error(e)

    async def orm_update(self, orm: TenantDB, data: TenantUpdateDTO) -> TenantDB:
        if data.name:
            orm.name = data.name

        if data.type:
            orm.type = data.type

        if data.status:
            orm.status = data.status

        if data.is_active:
            orm.is_active = data.is_active

        return orm

    async def delete(self):
        return
