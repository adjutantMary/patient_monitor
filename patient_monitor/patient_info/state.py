import reflex as rx
from typing import Optional, List
from sqlmodel import select

from ..db.models.patient import Patient
from ..api.base_models import PatientBase
from ..db.managers import PatientManager


class PatientInfoState(rx.State):
    
    '''Стейт для описания детальной информации по пациентам по лотус айдишнику'''
    
    patients: List['Patient'] = []
    patient: Optional['Patient'] = None
    patient_mh: List = []
    
    @rx.var
    def patient_lotus_id(self):
        return self.router.page.params.get("lotus_id", "")

    def load_patients(self):
        with rx.session() as session:
            result = session.exec(
                select(PatientBase)
            ).all()
            self.patients = result
        
    def load_medical_histories(self):
        # начала работать с подргрузкой медицинский историй пациента. не запускала эту функцию
        pm = PatientManager()
        self.patient_mh = [patient.dict() for patient in pm.get_all_medical_histories()]
        print(self.patient_mh)
        
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

