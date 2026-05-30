from pydantic import BaseModel
from uuid import UUID
from src.features.tenant.enums.tenant import TenantType, TenantStatus


class CreateTenant(BaseModel):
    name: str
    type: TenantType


class ReadTenant(BaseModel):
    id: UUID
    name: str
    type: TenantType
    status: TenantStatus
    is_active: bool

    model_config = {"from_attributes": True}
