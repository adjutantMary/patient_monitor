import reflex as rx
from .pages import index
from .api import *
from .db.models import *

app = rx.App()
app.add_page(index)
app.api.add_api_route("/patient", get_patient)
app.api.add_api_route("/patient", create_patient, methods=["POST"])