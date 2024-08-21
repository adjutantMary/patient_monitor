from pydantic import BaseModel
from datetime import date, datetime


# Базы данных для FastAPI

class PatientBase(BaseModel):
    lotus_id: str
    fio: str
    birthday: date
    is_man: bool
    

class PatientsListBase(BaseModel):
    patients: list[PatientBase] | None
    
    
# старый вариант бд
# class MedicalHistoryBase(BaseModel):
#     patient_lotus_id: str | None = None
#     patient_id: str | None = None
#     is_active:bool = False
#     lotus_id: str
#     number: str
#     current_department_name: str
#     income_datetime: datetime
#     outcome_datetime: datetime | None = None
#     created_at: datetime = None
#     updated_at: datetime = None
    

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