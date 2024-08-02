import reflex as rx
from ..api.base_models import PatientBase
from ..db.managers import PatientManager

class PatientListState(rx.State):
    patients: list[PatientBase] = []
    
    def load_entries(self):
        pm = PatientManager()
        self.patients = [patient.dict() for patient in pm.get_all_patients()]
    
    