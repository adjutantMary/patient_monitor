import reflex as rx
from sqlmodel import Field, Relationship
import sqlalchemy as sa
from uuid import UUID, uuid4
from datetime import datetime, date
from typing import Optional, List

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
    
    medical_histories: List["MedicalHistory"] = Relationship(
        back_populates="patient"
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
    

class MedicalHistory(rx.Model, table=True):
    __tablename__ ='medical_history'
    
    id: UUID = Field(
        default=None,
        sa_column=sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            primary_key=True,
            default=uuid4,
        ),
    )
    patient_id: UUID = Field(foreign_key="patient.id") 
    patient: Optional[Patient] = Relationship(
        back_populates="medical_histories"
    )
    
    is_active: bool = Field(default=False)
    lotus_id: str
    number: str
    current_department_name: str
    
    income_date: date = Field(
        default=None,
        sa_column=sa.Column(
            "income_date",
            sa.Date()
        )
    )
    outcome_date: date = Field(
        default=None,
        sa_column=sa.Column(
            "outcome_date",
            sa.Date(),
            nullable=True
        ),
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
        d["income_date"] = self.income_date.isoformat()
        d["outcome_date"] = self.outcome_date.isoformat()
        d["patient_id"] = str(self.patient_id)
        d["created_at"] = self.created_at.replace(
                microsecond=0
            ).isoformat()
        d["updated_at"] = self.updated_at.replace(
                microsecond=0
            ).isoformat()
        return d
    
class Diagnosis(rx.Model, table=True):
    __tablename__ = 'diagnosis'
    
    id: UUID = Field(
        default=None,
        sa_column=sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            primary_key=True,
            default=uuid4,
        ),
    )
    
    main_issue: str
    mkb: str
    ksg: str
    standart:str
    
    diagnosis_type_id: int = Field(foreign_key="diagnosis_type.id")
    diagnosis_type: Optional["DiagnosisType"] = Relationship(
        back_populates="diagnosis"
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
        d["patient_id"] = str(self.patient_id)
        d["created_at"] = self.created_at.replace(
                microsecond=0
            ).isoformat()
        d["updated_at"] = self.updated_at.replace(
                microsecond=0
            ).isoformat()
        return d
    
class DiagnosisType(rx.Model, table=True):
    __tablename__ = 'diagnosis_type'
    
    name: str
    
    diagnosis: List["Diagnosis"] = Relationship(
        back_populates="diagnosis_type"
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
        d["created_at"] = self.created_at.replace(
                microsecond=0
            ).isoformat()
        d["updated_at"] = self.updated_at.replace(
                microsecond=0
            ).isoformat()
        d["qwe"] = 1
        return d
    
