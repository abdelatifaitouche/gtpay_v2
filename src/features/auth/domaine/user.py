from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    email: str
    password_hash: str


@dataclass
class BaseUser:
    id: UUID
    email: str
