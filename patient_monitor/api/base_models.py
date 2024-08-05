from pydantic import BaseModel
from datetime import date, datetime

class PatientBase(BaseModel):
    lotus_id: str
    fio: str
    birthday: date
    is_man: bool
    

class PatientsListBase(BaseModel):
    patients: list[PatientBase] | None
    

class MedicalHistoryBase(BaseModel):
    patient_lotus_id: str | None = None
    patient_id: str | None = None
    is_active:bool = False
    lotus_id: str
    number: str
    current_department_name: str
    income_datetime: datetime
    outcome_datetime: datetime | None = None
    created_at: datetime = None
    updated_at: datetime = None
    
class MedicalHistoryListBase(BaseModel):
    mh_list: list[MedicalHistoryBase] | None = None