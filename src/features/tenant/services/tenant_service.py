from uuid import UUID
from src.features.tenant.repositories.tenant_repository import TenantRepository
from src.features.tenant.domaine.tenant import (
    Tenant as TenantEntity,
    CreateTenant as CreateTenantEntity,
)


class TenantService:
    def __init__(self, repo: TenantRepository):
        self.repo: TenantRepository = repo

    async def list(self) -> list[TenantEntity]:
        tenants = await self.repo.list()
        return tenants

    async def create_tenant(self, data: CreateTenantEntity) -> TenantEntity:
        tenant: TenantEntity = await self.repo.save(data)
        return tenant

    async def get_by_id(self, tenant_id: UUID) -> TenantEntity:
        return await self.repo.get_by_id(tenant_id)
