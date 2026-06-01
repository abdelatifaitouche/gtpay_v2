from src.infra.db.base import Base
from src.infra.db.mixins import UUIDMixin, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, UniqueConstraint

from src.features.tenant.enums.tenant import TenantType


class Permission(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "permissions"

    resource: Mapped[str] = mapped_column(String(100), nullable=False)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    scope: Mapped[TenantType] = mapped_column(Enum(TenantType), nullable=False)

    __table_args__ = UniqueConstraint(
        "resource", "action", name="uq_permission_resource_action"
    )
