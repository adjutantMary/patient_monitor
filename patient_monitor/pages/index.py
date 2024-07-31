import reflex as rx
from .base import base_page
from ..data.routes import PATIENT_ROUTE
from typing import List

class ForeachState(rx.State):
    patients: List[tuple[str, str]] = [
        ("Иванов Иван Иванович", "Диагноз Ивана"),
        ("Иванов Иван Иванович", "Диагноз Ивана"),
        ("Иванов Иван Иванович", "Диагноз Ивана"),
        ("Иванов Иван Иванович", "Диагноз Ивана"),
        ("Иванов Иван Иванович", "Диагноз Ивана"),
        ("Иванов Иван Иванович", "Диагноз Ивана"),
    ]

def patient_list_element(data:tuple) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(data[0], size="4", weight="medium"), href=PATIENT_ROUTE
        ),
        rx.text(data[1], size="4", weight="medium"),
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