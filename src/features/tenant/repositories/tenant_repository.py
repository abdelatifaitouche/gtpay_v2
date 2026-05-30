from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from src.features.tenant.domaine.tenant import (
    Tenant as TenantEntity,
    CreateTenant as CreateTenantEntity,
)
from src.features.tenant.models.tenant import Tenant as TenantDB


class TenantRepository:
    model = TenantDB

    def __init__(self, db: AsyncSession):
        self.db: AsyncSession = db

    def to_orm(self, tenant: CreateTenantEntity) -> TenantDB:
        return TenantDB(
            name=tenant.name,
            type=tenant.type,
        )

    def to_domain(self, orm: TenantDB) -> TenantEntity:
        return TenantEntity(
            id=orm.id,
            name=orm.name,
            type=orm.type,
            status=orm.status,
            is_active=orm.is_active,
        )

    async def save(self, tenant: CreateTenantEntity) -> TenantEntity:
        orm: TenantDB = self.to_orm(tenant)
        self.db.add(orm)
        await self.db.flush()
        return self.to_domain(orm)

    async def list(self) -> list[TenantEntity]:
        stmt = select(self.model)
        results = await self.db.execute(stmt)
        data = results.scalars().all()
        return [self.to_domain(obj) for obj in data]

    async def get_by_id(self, tenant_id: UUID) -> TenantEntity:
        stmt = select(self.model).where(self.model.id == tenant_id)
        result = await self.db.execute(stmt)
        data = result.scalar_one()
        return self.to_domain(data)

    async def update(self):
        return

    async def delete(self):
        return
