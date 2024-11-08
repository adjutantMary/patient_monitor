import reflex as rx
from .base import base_page
from ..api.base_models import *
from ..db.managers import *
from typing import List


def index() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.text(
                "Нужно придумать что мы тут будем хранить",
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            text_align="center",
            align="center",
        )
    )