from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.uow import get_db
from src.features.tenant.services.tenant_service import TenantService
from src.features.tenant.repositories.tenant_repository import TenantRepository
from src.features.tenant.schemas.tenant import CreateTenant, ReadTenant, UpdateTenant
from src.features.tenant.mappers.tenant import TenantMapper

router = APIRouter(prefix="/tenants")


async def get_service(db: AsyncSession = Depends(get_db)):
    repo = TenantRepository(db)
    return TenantService(repo)


@router.get("")
async def list(service: TenantService = Depends(get_service)):
    tenants = await service.list()
    return [ReadTenant.model_validate(t) for t in tenants]


@router.post("/")
async def create(data: CreateTenant, service: TenantService = Depends(get_service)):
    tenant = await service.create_tenant(TenantMapper.from_create_schema(data))
    return ReadTenant.model_validate(tenant)


@router.get("/{tenant_id}")
async def get_by_id(tenant_id: str, service: TenantService = Depends(get_service)):
    tenant = await service.get_by_id(UUID(tenant_id))
    return tenant


@router.patch("/{tenant_id}/")
async def update_tenant(
    tenant_id: str,
    data: UpdateTenant,
    service: TenantService = Depends(get_service),
):
    tenant = await service.update(UUID(tenant_id), TenantMapper.to_update_dto(data))
    return tenant


@router.patch("/{tenant_id}/suspend/")
async def suspend_tenant(
    tenant_id: str,
    service: TenantService = Depends(
        get_service,
    ),
):
    tenant = await service.suspend_tenant(UUID(tenant_id))
    return ReadTenant.model_validate(tenant)
