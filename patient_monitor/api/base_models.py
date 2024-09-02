from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional


# Базы данных для FastAPI

class PatientBase(BaseModel):
    lotus_id: str
    fio: str
    birthday: date
    is_man: bool
    

class PatientsListBase(BaseModel):
    patients: list[PatientBase] | None


class PostMedicatHistoryBase(BaseModel):
    '''Модель медисторий по вводу данных в базу'''
    lotus_id: str
    patient_lotus_id: str | None = None
    patient_id: str | None = None
    is_active:bool = False
    number: str
    current_department_name: str
    income_datetime: datetime
    outcome_datetime: datetime | None = None
    created_at: datetime = None 
    updated_at: datetime = None


class GetMedicalHistoryBase(BaseModel):
    '''Модель медисторий по выводу данных из базы'''
    patient_lotus_id: str | None = None
    patient_id: str | None = None
    lotus_id: str
    
    
class PostHistoryListBase(BaseModel):
    mh_list: list[PostMedicatHistoryBase] | None = None
    
class GetHistoryListBase(BaseModel):
    mh_list: list[GetMedicalHistoryBase] | None = None
    
class DiagnosisTypeBase(BaseModel):
# застряла на этапе отношений поля diagnosis с DiagnosisBase. one to many?
        name: str
        diagnosis: List["DiagnosisBase"] | None
        created_at: datetime = None 
        updated_at: datetime = None

class DiagnosisBase(BaseModel):
    # для этой схемы получилось создать экземпляр в бдшке
    main_issue: str
    mkb: str
    ksg: str
    standart: str
    diagnosis_type_id: int
    diagnosis_type: Optional["DiagnosisTypeBase"] | None
    created_at: datetime = None 
    updated_at: datetime = None
    

    
class DiagnosisListBase(BaseModel):
    diagnosis: list[DiagnosisBase] | None

class DiagnosisTypeListBase(BaseModel):
    dt_list: list[DiagnosisTypeBase] | None