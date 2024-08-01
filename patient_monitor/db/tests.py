from datetime import date
from ..db.managers import *

pm = PatientManager()

test_patient = PatientBase(
    lotus_id="324123",
    fio="Иванов Иван Иванович",
    birthday=date(2000, 9, 30),
    is_man=True
)



# from patient_monitor.db.tests import *