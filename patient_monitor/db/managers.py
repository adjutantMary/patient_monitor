import reflex as rx
from ..api.base_models import PatientBase
from ..db.models import Patient
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

class PatientManager:
    def create_patient(self, patient_data:PatientBase):
        with rx.session() as session:
            patient = Patient(
                fio=patient_data.fio,
                lotus_id=patient_data.lotus_id,
                birthday=patient_data.birthday,
                is_man=patient_data.is_man,
            )
            session.add(patient)
            try:
                session.commit()
            except IntegrityError:
                return None
            session.refresh(patient)
            return patient
    
    def get_patient_by_lotus_id(self, lotus_id:str):
        with rx.session() as session:
            return session.exec(
                select(Patient)
                .where(Patient.lotus_id == lotus_id)
            ).first()
            
    def get_all_patients(self):
        with rx.session() as session:
            return session.exec(
                select(Patient)
            ).all()
             
        
    