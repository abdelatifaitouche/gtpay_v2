from src.core.common.scope import Scope


class TenantPermissions:
    CREATE = ("tenants", "create", Scope.PLATFORM)
    READ = ("tenants", "read", Scope.PLATFORM)
    UPDATE = ("tenants", "update", Scope.PLATFORM)
    SUSPEND = ("tenants", "suspend", Scope.PLATFORM)
    ACTIVATE = ("tenants", "activate", Scope.PLATFORM)
    DELETE = ("tenants", "delete", Scope.PLATFORM)
