from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    lotus_id: str
    fio: str
    birthday: date
    is_man: bool
    
