import reflex as rx
from ..api.base_models import *
from ..db.models import *
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc, asc

class PatientManager:
    def create_patient(self, patient_data:PatientBase):
        with rx.session() as session:
            patient = Patient(
                fio=patient_data.fio,
                lotus_id=patient_data.lotus_id,
                birthday=patient_data.birthday,
                is_man=patient_data.is_man,
            )
            session.add(patient)
            try:
                session.commit()
            except IntegrityError:
                return None
            session.refresh(patient)
            return patient
    
    def get_patient_by_lotus_id(self, lotus_id:str):
        with rx.session() as session:
            return session.exec(
                select(Patient)
                .where(Patient.lotus_id == lotus_id)
            ).first()
            
    def get_all_patients(self):
        with rx.session() as session:
            return session.exec(
                select(Patient)
            ).all()

    def get_all_medical_histories(self, patient_id:str):
        with rx.session() as session:
            patient = self.get_patient_by_lotus_id(lotus_id=patient_id)
            return session.exec(
                select(MedicalHistory).
                where(MedicalHistory.patient_id == patient.id)
            ).all()
    
    
    def get_active_medical_history(self, patient_id:str):
        '''Фильтрация мед историй по активности: True/False'''
        with rx.session() as session:
            patient = self.get_patient_by_lotus_id(lotus_id=patient_id)
            mh = session.exec(
                select(MedicalHistory).filter(MedicalHistory.is_active == True, MedicalHistory.patient_id == patient.id)
            ).first()
            return mh    
        
class MedicalHistoryManager:
    def create_medical_history(self, mh_data: PostMedicatHistoryBase):
        with rx.session() as session:
            patient = PatientManager().get_patient_by_lotus_id(lotus_id=mh_data.patient_lotus_id)
            mh = MedicalHistory(
                patient_id=patient.id,
                is_active=mh_data.is_active,
                lotus_id=mh_data.lotus_id,
                number=mh_data.number,
                current_department_name=mh_data.current_department_name,
                income_datetime=mh_data.income_datetime,
                outcome_datetime=mh_data.outcome_datetime,
            )
            session.add(mh)
            try:
                session.commit()
            except IntegrityError as e:
                print(e)
                return None
            session.refresh(mh)
            return mh
    
    def get_medical_history_by_lotus_id(self, lotus_id:str):
        with rx.session() as session:
            return session.exec(
                select(MedicalHistory)
                .where(MedicalHistory.lotus_id == lotus_id)
            ).first()
            
    def get_medical_history_by_id(self, id:str):
        with rx.session() as session:
            return session.exec(
                select(MedicalHistory)
                .where(MedicalHistory.id == id)
            ).first()

class DiagnosisManager:
    """ менеджер апи запросов к диагнозам """
    def create_diagnosis(self, d_data: DiagnosisBase):
        with rx.session() as session:
            d_base = Diagnosis(
                main_issue=d_data.main_issue,
                mkb=d_data.mkb,
                ksg=d_data.ksg,
                standart=d_data.standart,
                diagnosis_type=d_data.diagnosis_type,
                diagnosis_type_id=d_data.diagnosis_type_id,
                created_at=d_data.created_at,
                updated_at=d_data.updated_at
            )
            session.add(d_base)
            try:
                session.commit()
            except IntegrityError as e:
                print(e)
                return None
            session.refresh(d_base)
            return d_base
    
    def get_diagnosis_list(self):
        with rx.session() as session:
            return session.exec(
                select(Diagnosis)
            ).all()
            
    def get_diagnosis_by_type_id(self, diagnosis_type_id: str):
        with rx.session() as session:
            return session.exec(
                select(Diagnosis)
                .where(Diagnosis.diagnosis_type_id == diagnosis_type_id)
            ).all()


class DiagnosisTypeManager:
    """ менеджер апи запросов к типам диагнозов """
    def create_diagnosis_type(self, dt_data: DiagnosisTypeBase):
        with rx.session() as session:
            dt_base = DiagnosisType(
                name=dt_data.name,
                diagnosis=dt_data.diagnosis,
                created_at=dt_data.created_at,
                updated_at=dt_data.updated_at
            
            )
            session.add(dt_base)
            try:
                session.commit()
            except IntegrityError as e:
                print(e)
                return None
            session.refresh(dt_base)
            return dt_base
    
    def get_diagnosis_list(self):
        with rx.session() as session:
            return session.exec(
                select(DiagnosisType)
            ).all()


class PatientParametricsManager:
    def create_patient_parametrics(self, mh_id:str, pp_data: PatientParametricsBase):
        pp_data_dict = pp_data.model_dump(by_alias=True) 
        with rx.session() as session:
            parametrics = PatientParametrics(
                **pp_data_dict,
                mh_id=mh_id,
            )
            session.add(parametrics)
            try:
                session.commit()
            except Exception as e:
                print(e)
            session.refresh(parametrics)
            return parametrics
            
    def get_all_patient_parametric(self, mh_id:str):
        with rx.session() as session:
            return session.exec(
                select(PatientParametrics)
                .where(PatientParametrics.mh_id == mh_id)
                .order_by(desc(PatientParametrics.check_datetime))
            ).all()

