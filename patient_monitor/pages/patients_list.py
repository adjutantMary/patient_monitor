import reflex as rx
from .base import base_page
from ..api.base_models import *
from ..db.managers import *
from typing import List



def patients_list() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.text(
                "Тут функциональная таблица с пациентами из базы",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            text_align="center",
            align="center",
        )
    )