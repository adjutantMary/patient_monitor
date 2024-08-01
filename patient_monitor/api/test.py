import reflex as rx
from ..db.managers import PatientManager

async def create_patient():
    return {"my_result": "PONG!"}

async def get_patient(lotus_id:str):
    pm = PatientManager()
    return pm.get_patient_by_lotus_id(lotus_id=lotus_id).dict()

