from uuid import UUID
from src.features.tenant.repositories.tenant_repository import TenantRepository
from src.features.tenant.domaine.tenant import (
    Tenant as TenantEntity,
    CreateTenant as CreateTenantEntity,
    TenantUpdate as TenantUpdateDTO,
)
from src.features.tenant.enums.tenant import TenantStatus, TenantType
from src.core.exceptions import ValidationError


class TenantService:
    def __init__(self, repo: TenantRepository):
        self.repo: TenantRepository = repo

    async def list(self) -> list[TenantEntity]:
        tenants = await self.repo.list()
        return tenants

    async def create_tenant(self, data: CreateTenantEntity) -> TenantEntity:
        entity = TenantEntity(
            name=data.name,
            type=data.type,
        )
        tenant: TenantEntity = await self.repo.save(entity)
        return tenant

    async def get_by_id(self, tenant_id: UUID) -> TenantEntity:
        return await self.repo.get_by_id(tenant_id)

    async def update(self, tenant_id: UUID, data: TenantUpdateDTO):
        entity: TenantEntity = await self.repo.get_by_id(tenant_id)

        return await self.__apply_update(entity, data)

    async def suspend_tenant(self, tenant_id: UUID):
        entity: TenantEntity = await self.repo.get_by_id(tenant_id)

        if not entity.is_active:
            raise ValidationError(
                "Cannot Suspend, Tenant Is deactivated",
            )

        if entity.type == TenantType.PLATFORM:
            raise ValidationError(
                "Cannot Suspend Platform tenant",
            )

        if entity.status in (TenantStatus.SUSPENDED, TenantStatus.DELETED):
            raise ValidationError(
                "Tenant Already Suspended",
            )

        entity.status = TenantStatus.SUSPENDED
        return await self.repo.save(entity)

    async def __apply_update(self, entity: TenantEntity, data: TenantUpdateDTO):
        if data.name:
            entity.name = data.name

        if data.type:
            entity.type = data.type

        return await self.repo.save(entity)
