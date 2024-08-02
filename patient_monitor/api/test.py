import reflex as rx
from ..db.managers import PatientManager
from ..api.base_models import PatientBase, PatientsListBase


async def get_patient(lotus_id:str):
    pm = PatientManager()
    return pm.get_patient_by_lotus_id(lotus_id=lotus_id).dict()

async def get_all_patient() -> PatientsListBase:
    pm = PatientManager()
    patients = pm.get_all_patients()
    return PatientsListBase(patients=[patient.dict() for patient in patients])
    

async def create_patient(patient_data: PatientBase):
    pm = PatientManager()
    patient = pm.create_patient(patient_data=patient_data)
    return patient.dict() if patient else {"message": "пациент с таким lotus_id уже существует"}

