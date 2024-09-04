import reflex as rx
from .base import base_page
from ..api.base_models import *
from ..db.managers import *
from typing import List
from ..states.patients_list import PatientListState



def show_patient(patient: Patient):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(
            rx.link(
                patient.fio,
                href="/patient/"
            )
        ),
        rx.table.cell(patient.birthday),
        rx.table.cell(rx.cond(patient.is_man, rx.icon("person-standing", color="blue"), rx.icon("person-standing", color="deeppink"))),
    )



def patients_list() -> rx.Component:
    return base_page(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ФИО"),
                    rx.table.column_header_cell("ДР"),
                    rx.table.column_header_cell("Пол"),
                ),
            ),
            rx.table.body(
                
            ),
            on_mount=PatientListState.load_entries
            width="100%",
            variant="surface",
        )
    )