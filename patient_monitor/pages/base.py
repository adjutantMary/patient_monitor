import reflex as rx
from ..components.navbar import navbar

def base_page(child: rx.Component, hide_navbar:bool=False, *args) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("Not a valid child element")
    if hide_navbar:
        return rx.container(
            child,
        )
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            padding="1em",
            width="100%", 
        ),
    )