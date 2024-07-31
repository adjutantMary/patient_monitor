import reflex as rx
from ..data import routes
from ..states.nav_state import NavState

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    href=routes.HOME_ROUTE,
                    ),
                rx.hstack(
                    navbar_link("Все пациенты", routes.HOME_ROUTE),
                    navbar_link("Мои пациенты", routes.ABOUT_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id="pc_navbar"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    href=routes.HOME_ROUTE,
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=NavState.to_home),
                        rx.menu.item("About", on_click=NavState.to_about),
                        rx.menu.item("Pricing", on_click=NavState.to_pricing),
                        rx.menu.item("Contact", on_click=NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id="navbar",
    )
