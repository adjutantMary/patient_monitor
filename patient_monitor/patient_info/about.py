import reflex as rx

from ..pages.base import base_page
from ..api.base_models import PatientBase

from . import state



# @rx.page(route='/patient/[id]')
def patient_detail_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading(
            f"Состояние пациента: {state.PatientInfoState.patient.fio}",
            size='5',
            align='left',
            weight='bold',
            
            ),
        rx.text(
            f"Лотус-id: {state.PatientInfoState.patient_lotus_id}",
            align="right"
        ),
        rx.text(
            "Круто классно работает",
        ),
        # spacing="5",
        # justify="center",
        # # align='center',
        # min_height='85vh',
        id="my_child"
    )
    return base_page(my_child)