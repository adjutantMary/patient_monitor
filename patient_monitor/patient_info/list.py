import reflex as rx

from . import state
from ..db import models

from .. import navigation

from ..pages import base_page




def patient_detail_link(child: rx.Component, patient: models.Patient):
    if patient is None:
        return rx.fragment(child)
    patient_id = patient.id
    if patient_id is None:
        return rx.fragment(child)
    rout_path = navigation.routes.PATIENT_INFO_ROUTE
    patient_detail_url = f"{rout_path}/{patient_id}"
    return rx.link(
        child,
        href=patient_detail_url
    )
    
def patient_detail_item(patient: models.Patient):
    return rx.box(
        patient_detail_link(
            rx.heading(patient.fio),
            patient
        ),
        padding='1em'
    )

def patient_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Patients", size="5"),
            rx.link(
                rx.button("Пиу Пау"),
                href=navigation.routes.PATIENT_INFO_ROUTE
            ),
            rx.foreach(state.PatientInfoState.patients,
                       patient_detail_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )
