import reflex as rx
from .pages import *
from .api import *
from .db.models import *
from .navigation.nav_state import NavState
from .navigation import routes

app = rx.App()
app.add_page(index)
app.add_page(patients_list, route=routes.PATIENTS_LIST_ROUTE)



app.api.add_api_route("/patient", get_patient)
app.api.add_api_route("/patient", create_patient, methods=["POST"])
app.api.add_api_route("/patient/all", get_all_patient)