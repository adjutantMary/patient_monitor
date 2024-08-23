import reflex as rx
from typing import Optional, List
from sqlmodel import select

from ..db.models import Patient


class PatientInfoState(rx.State):
    
    patients: List['Patient'] = []
    patient: Optional['Patient'] = None

    def load_patients(self):
        with rx.session() as session:
            result = session.exec(
                select(Patient)
            ).all()
            self.patients = result
            
    # def load_patient_by_id(self):
    #     pass
            
    # def app_patient(self):
    #     pass