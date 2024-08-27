import reflex as rx
from typing import Optional, List
from sqlmodel import select

from ..db.models.patient import Patient
from ..api.base_models import PatientBase


class PatientInfoState(rx.State):
    
    '''Стейт для описания детальной информации по пациентам по лотус айдишнику'''
    
    patients: List['Patient'] = []
    patient: Optional['Patient'] = None
    
    @rx.var
    def patient_lotus_id(self):
        return self.router.page.params.get("lotus_id", "")

    def load_patients(self):
        with rx.session() as session:
            result = session.exec(
                select(PatientBase)
            ).all()
            self.patients = result
            
    def get_detail_patient_info(self):
        with rx.session() as session:
            if self.patient_lotus_id == "":
                self.patient = None
                return 
            result = session.exec(
                select(Patient).where(
                    Patient.lotus_id == self.patient_lotus_id
                )
            ).one_or_none()
            self.patient = result
