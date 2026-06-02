from src.infra.db.base import Base
from src.infra.db.mixins import UUIDMixin, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, UniqueConstraint

from src.core.common.scope import Scope


class Permission(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "permissions"

    resource: Mapped[str] = mapped_column(String(100), nullable=False)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    scope: Mapped[Scope] = mapped_column(
        Enum(Scope), nullable=False, default=Scope.CLIENT
    )

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        "RolePermission", back_populates="permission", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("resource", "action", name="uq_permission_resource_action"),
    )
