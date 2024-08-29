import reflex as rx
from ..api.base_models import *
from ..db.models import *
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

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
            return session.exec(
                select(MedicalHistory).filter(MedicalHistory.is_active == True, MedicalHistory.patient_id == patient.id)
            ).all()
    
        
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
            

class DiagnosisManager:
    """ менеджер апи запросов к диагнозам """
    def create_diagnosis(self, diagnosis_data: DiagnosisBase):
        with rx.session() as session:
            d_base = Diagnosis(
                main_issue=diagnosis_data.main_issue,
                mkb=diagnosis_data.mkb,
                ksg=diagnosis_data.ksg,
                standart=diagnosis_data.standart,
                diagnosis_type=diagnosis_data.diagnosis_type,
                diagnosis_type_id=diagnosis_data.diagnosis_type_id,
                created_at=diagnosis_data.created_at,
                updated_at=diagnosis_data.updated_at
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
    