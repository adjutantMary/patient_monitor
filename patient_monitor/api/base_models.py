import reflex as rx
from datetime import date

class PatientBase(rx.Base):
    lotus_id: str
    fio: str
    birthday: date
    is_man: bool