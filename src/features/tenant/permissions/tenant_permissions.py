from src.features.tenant.enums.tenant import TenantType


class TenantPermissions:
    CREATE = ("tenants", "create", TenantType.PLATFORM)
    READ = ("tenants", "read", TenantType.PLATFORM)
    UPDATE = ("tenants", "update", TenantType.PLATFORM)
    SUSPEND = ("tenants", "suspend", TenantType.PLATFORM)
    ACTIVATE = ("tenants", "activate", TenantType.PLATFORM)
    DELETE = ("tenants", "delete", TenantType.PLATFORM)
