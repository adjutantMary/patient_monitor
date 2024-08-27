import reflex as rx

from ..pages.base import base_page
from ..api.base_models import PatientBase

from . import state


# @rx.page(route='/patient/[id]')
def patient_detail_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading(state.PatientInfoState.patient.fio, size='9'),
        rx.text(
            state.PatientInfoState.patient_lotus_id
        ),
        rx.text(
            "Круто классно работает",
        ),
        spacing="5",
        justify="center",
        align='center',
        min_height='85vh',
        id="my_child"
    )
    return base_page(my_child)