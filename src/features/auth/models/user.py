from src.infra.db.base import Base
from src.infra.db.mixins import TimestampMixin, UUIDMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)

    is_active: Mapped[bool] = mapped_column(default=True)
