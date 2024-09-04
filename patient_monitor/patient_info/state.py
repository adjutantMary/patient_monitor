import reflex as rx
from typing import Optional, List
from sqlmodel import select

from ..db.models.patient import Patient
from ..api.base_models import PatientBase
from ..db.managers import PatientManager


class PatientInfoState(rx.State):
    
    '''Стейт для описания детальной информации по пациентам по лотус айдишнику'''
    
    patients: List["Patient"]
    patient: Optional['Patient'] = None
    patient_mh: List = []
    patient_id: str = None
    
    @rx.var
    def patient_lotus_id(self):
        return self.router.page.params.get("id", "")
    
    @rx.var
    def patient_id_str(self) -> str:
        if self.patient is None:
            return ""
        return str(self.patient.id)

    @rx.var
    def _patient_id(self):
        return self.router.page.params.get("id", "")
    
    def load_patient_id(self):
        with rx.session() as session:
            result = session.exec(
                select(Patient.id)
            ).one_or_none()
            self.patient_id = result
    
    def load_patients(self):
        with rx.session() as session:
            result = session.exec(
                select(PatientBase)
            ).all()
            self.patients = result
        
    def load_medical_histories(self):
        pm = PatientManager()
        patient_id = self.patient_id
        for medical_history in pm.get_all_medical_histories(patient_id=patient_id):
            if patient_id == "":
                medical_history = None
                return
            self.patient_mh = dict(medical_history)
        
        # pm = PatientManager()
        # self.patient_mh = [patient.dict() for patient in pm.get_all_medical_histories(self.patient_lotus_id)]
        # print(self.patient_mh)
        # pass
        
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

