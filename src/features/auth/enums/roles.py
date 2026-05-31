from enum import StrEnum


class Roles(StrEnum):
    # PLATFORM USERS
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    OPERATOR = "OPERATOR"
    # CLIENT
    CLIENT = "CLIENT"
    EMPLOYEE = "EMPLOYEE"
