from src.infra.db.base import Base
from src.infra.db.mixins import TimestampMixin, UUIDMixin
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey


class User(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id"), nullable=False, index=True
    )

    is_active: Mapped[bool] = mapped_column(default=True)

    tenant: Mapped["Tenant"] = relationship(back_populates="users")
