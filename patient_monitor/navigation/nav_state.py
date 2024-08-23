import reflex as rx
from . import routes

class NavState(rx.State):
    
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_patients_list(self):
        return rx.redirect(routes.PATIENTS_LIST_ROUTE)
    
    def to_patient(self):
        return rx.redirect(routes.PATIETN_INFO_ROUTE)