from src.core.permissions import Permissions
from src.features.tenant.enums.tenant import TenantType
import inspect


def get_all_permissions() -> list[tuple[str, str, TenantType]]:
    all_perms = []

    for feature_class in vars(Permissions).values():
        if inspect.isclass(feature_class):
            for val in vars(feature_class).values():
                if isinstance(val, tuple) and len(val) == 3:
                    all_perms.append(val)

    return all_perms
