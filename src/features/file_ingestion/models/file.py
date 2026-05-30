"""
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


from src.infra.db.base import Base
from src.infra.db.mixins import UUIDMixin, TimestampMixin
from src.features.file_ingestion.enums.file import FileState


class File(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "files"

    matricule: str
    original_filename: str
    storage_key: str
    bucket: str
    state: FileState
    is_encrypted: bool
    is_virus_scanned: bool
    is_infected: bool
    mime_type: str
    size_bytes: str

    # add later, checksum, tenantid, and some data to check whether it has an employee or not
"""
