import reflex as rx
from .pages import *
from .api import *
from .db.models import *
from .navigation.nav_state import NavState
from .navigation import routes
from . import patient_info, navigation

app = rx.App()
app.add_page(index)
app.add_page(patients_list, route=routes.PATIENTS_LIST_ROUTE)

app.add_page(patient_info.patient_list_page,
             route=navigation.routes.PATIENT_INFO_ROUTE,
             on_load=patient_info.PatientInfoState.load_patients
)



app.api.add_api_route("/patient", get_patient)
app.api.add_api_route("/patient", create_patient, methods=["POST"])
app.api.add_api_route("/patient/all", get_all_patient)
app.api.add_api_route("/med-history", create_mh, methods=["POST"])
app.api.add_api_route("/med-history", get_mh)
app.api.add_api_route("/med-history/all", get_all_mh)
app.api.add_api_route("/med-history/active", get_active_mh)