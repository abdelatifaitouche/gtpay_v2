from src.infra.db.mixins import TimestampMixin, UUIDMixin
from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, Boolean
from src.features.tenant.enums.tenant import TenantType, TenantStatus


class Tenant(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "tenants"

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)

    type: Mapped[TenantType] = mapped_column(
        Enum(TenantType),
        nullable=False,
        index=True,
    )

    status: Mapped[TenantStatus] = mapped_column(
        Enum(TenantStatus),
        nullable=False,
        default=TenantStatus.ACTIVE,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="tenant", cascade="all, delete-orphan"
    )
