from src.core.common.scope import Scope
from enum import StrEnum


class Role(StrEnum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    OPERATOR = "OPERATOR"
    CLIENT = "CLIENT"
    EMPLOYEE = "EMPLOYEE"


ROLES = [
    (
        Role.SUPER_ADMIN,
        Scope.PLATFORM,
    ),
    (
        Role.ADMIN,
        Scope.PLATFORM,
    ),
    (
        Role.MANAGER,
        Scope.PLATFORM,
    ),
    (
        Role.OPERATOR,
        Scope.PLATFORM,
    ),
    (
        Role.CLIENT,
        Scope.CLIENT,
    ),
    (
        Role.EMPLOYEE,
        Scope.CLIENT,
    ),
]
