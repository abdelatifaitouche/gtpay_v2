from enum import StrEnum


class TenantType(StrEnum):
    PLATFORM = "PLATFORM"
    CLIENT = "CLIENT"


class TenantStatus(StrEnum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    DELETED = "DELETED"
