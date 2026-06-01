from src.infra.db.base import Base
from src.infra.db.mixins import UUIDMixin, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Enum
from src.features.tenant.enums.tenant import TenantType


class Role(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(40), unique=True)
    scope: Mapped[TenantType] = mapped_column(
        Enum(TenantType), default=TenantType.CLIENT, nullable=False
    )
    is_system: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
