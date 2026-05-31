from dataclasses import dataclass
from uuid import UUID
from src.features.tenant.enums.tenant import TenantType, TenantStatus


@dataclass
class CreateTenant:
    name: str
    type: TenantType


@dataclass
class Tenant:
    name: str
    type: TenantType
    status: TenantStatus | None = None
    is_active: bool | None = None
    id: UUID | None = None


@dataclass
class TenantUpdate:
    name: str | None = None
    type: TenantType | None = None
    status: TenantStatus | None = None
    is_active: bool | None = None
