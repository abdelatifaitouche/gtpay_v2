from src.infra.db.base import Base
from src.infra.db.mixins import UUIDMixin, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Enum
from src.core.common.scope import Scope


class Role(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(40), unique=True)
    scope: Mapped[Scope] = mapped_column(
        Enum(Scope, name="role_scope", create_type=False),
        default=Scope.CLIENT,
        nullable=False,
    )
    is_system: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        "RolePermission",
        back_populates="role",
        cascade="all, delete-orphan",
    )
