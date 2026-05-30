from dataclasses import dataclass
from uuid import UUID
from src.features.tenant.enums.tenant import TenantType, TenantStatus


@dataclass
class CreateTenant:
    name: str
    type: TenantType


@dataclass
class Tenant:
    id: UUID
    name: str
    type: TenantType
    status: TenantStatus
    is_active: bool
