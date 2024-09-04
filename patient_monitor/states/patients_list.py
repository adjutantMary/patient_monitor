import reflex as rx
from ..api.base_models import PatientBase
from ..db.managers import PatientManager
from ..db.models.patient import Patient

class PatientListState(rx.State):
    patients: list["Patient"] = []
    
    def load_entries(self):
        pm = PatientManager()
        self.patients = [patient for patient in pm.get_all_patients()]

    
    