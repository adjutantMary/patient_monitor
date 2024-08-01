import reflex as rx
from sqlmodel import Field, Relationship
import sqlalchemy as sa
from uuid import UUID, uuid4
from datetime import datetime, date

class Patient(rx.Model, table=True):
    __tablename__ = 'patient'
    
    id: UUID = Field(
        default=None,
        sa_column=sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            primary_key=True,
            default=uuid4,
        ),
    )

    lotus_id: str = Field(
        unique=True
    )
    fio: str
    birthday: date = Field(
        default=None,
        sa_column=sa.Column(
            "birthday",
            sa.Date(),
        )
    )
    is_man : bool = Field(
        default=True
    )

    created_at: datetime = Field(
        default=None,
        sa_column=sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.now(),
        )
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            onupdate=sa.func.now()
        )
    )
    
    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["birthday"] = self.birthday.isoformat()
        d["created_at"] = self.created_at.replace(
                microsecond=0
            ).isoformat()
        d["updated_at"] = self.updated_at.replace(
                microsecond=0
            ).isoformat()
        return d