import reflex as rx
from reactflow  import react_flow

from ..pages.base import base_page
from ..api.base_models import PatientBase
from ..components.dragging_state import State

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
        rx.vstack(
            react_flow(
                nodes_draggable=True,
                nodes_connectable=True,
                on_nodes_change=lambda e0: State.on_nodes_change(
                    e0
                ),
                nodes=State.nodes,
                edges=State.edges,
                fit_view=True,
            )
        ),
        id="my_child",
        
    )
    return base_page(my_child)