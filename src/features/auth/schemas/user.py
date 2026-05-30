from pydantic import BaseModel
from uuid import UUID


class CreateUser(BaseModel):
    email: str
    password: str


class ReadUser(BaseModel):
    id: UUID
    email: str
