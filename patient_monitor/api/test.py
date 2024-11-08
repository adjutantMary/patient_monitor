import reflex as rx
from ..db.managers import *
from ..api.base_models import *


async def get_patient(lotus_id:str):
    pm = PatientManager()
    return pm.get_patient_by_lotus_id(lotus_id=lotus_id).dict()

async def get_all_patient() -> PatientsListBase:
    pm = PatientManager()
    patients = pm.get_all_patients()
    return PatientsListBase(patients=[patient.dict() for patient in patients])

async def create_patient(patient_data: PatientBase):
    pm = PatientManager()
    patient = pm.create_patient(patient_data=patient_data)
    return patient.dict() if patient else {"message": "пациент с таким lotus_id уже существует"}

async def create_mh(mh_data: PostMedicatHistoryBase):
    mhm = MedicalHistoryManager()
    mh = mhm.create_medical_history(mh_data=mh_data)
    return mh.dict() if mh else {"message": "история болезни с таким lotus_id уже существует"}

async def create_diagnosis_type(dt_data: DiagnosisTypeBase):
    dtm = DiagnosisTypeManager()
    diagnosis_type = dtm.create_diagnosis_type(dt_data=dt_data)
    return dtm.dict() if diagnosis_type else {"message": "не удалось создать тип диагноза"}

async def create_diagnosis(d_data: DiagnosisBase):
    dm = DiagnosisManager()
    diagnosis = dm.create_diagnosis_type(d_data=d_data)
    return dm.dict() if diagnosis else {"message": "не удалось создать диагноз"}

async def get_mh(lotus_id: str):
    mhm = MedicalHistoryManager()
    mh = mhm.get_medical_history_by_lotus_id(lotus_id=lotus_id)
    return mh.dict() if mh else {"message": "Истории болезни с такой lotus_id не существует"} 

async def get_all_mh(patient_id:str) -> GetHistoryListBase:
    pm = PatientManager()
    mh_list = pm.get_all_medical_histories(patient_id=patient_id)
    return GetHistoryListBase(mh_list=[mh.dict() for mh in mh_list])
    
async def get_active_mh(patient_id:str) -> GetHistoryListBase:
    '''Активные мед истории'''
    pm = PatientManager()
    mh_list = pm.get_active_medical_history(patient_id=patient_id)
    return GetHistoryListBase(mh_list=[mh.dict() for mh in mh_list])


async def create_parametrics(patient_lotus_id:str, pp_data: PatientParametricsBase)->PatientParametricsBase:
    mh = PatientManager().get_active_medical_history(patient_id=patient_lotus_id)
    mh_id = mh.id
    parametrics = PatientParametricsManager().create_patient_parametrics(mh_id=mh_id, pp_data=pp_data)
    return PatientParametricsBase(**parametrics.formated_dict())

async def get_patient_parametrics(patient_lotus_id:str) -> PatientParametricsListBase:
    mh = PatientManager().get_active_medical_history(patient_id=patient_lotus_id)
    mh_id = mh.id
    parametrics_list = PatientParametricsManager().get_all_patient_parametric(mh_id=mh_id)
    return PatientParametricsListBase(parametr_check_list=[params.formated_dict() for params in parametrics_list])