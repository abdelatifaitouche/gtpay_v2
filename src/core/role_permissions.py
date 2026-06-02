from src.core.roles import Role
from src.features.tenant.permissions.tenant_permissions import TenantPermissions

ROLE_PERMISSIONS = {
    Role.SUPER_ADMIN: [
        TenantPermissions.CREATE,
        TenantPermissions.READ,
        TenantPermissions.UPDATE,
        TenantPermissions.SUSPEND,
        TenantPermissions.ACTIVATE,
        TenantPermissions.DELETE,
    ],
    Role.ADMIN: [
        TenantPermissions.CREATE,
        TenantPermissions.READ,
        TenantPermissions.UPDATE,
        TenantPermissions.SUSPEND,
        TenantPermissions.ACTIVATE,
    ],
    Role.MANAGER: [
        TenantPermissions.READ,
    ],
    Role.OPERATOR: [
        TenantPermissions.READ,
    ],
    Role.CLIENT: [],
    Role.EMPLOYEE: [],
}
