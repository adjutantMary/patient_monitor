import reflex as rx
from .base import base_page
from ..data.routes import PATIENT_ROUTE
from ..api.base_models import *
from ..db.managers import *
from typing import List

class ForeachState(rx.State):

    @rx.var
    def patients(self) -> List[Patient]:
        pm = PatientManager()
        return pm.get_all_patients()

def patient_list_element(patient:Patient) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(patient.fio, size="4", weight="medium"), href=PATIENT_ROUTE
        ),
        rx.text(patient.lotus_id, size="4", weight="medium"),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.text(
                "Get started by editing ",
                size="5",
            ),
            rx.vstack(
                rx.foreach(
                    ForeachState.patients,
                    patient_list_element
                ),
                spacing="5",
                justify="center",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            text_align="center",
            align="center",
        )
    )