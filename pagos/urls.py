from django.urls import path
from . import views

app_name = "pagos"

urlpatterns = [
    path('pagarReserva/',   views.pagarReserva,   name="pagarReserva"),
    path('pagarServicio/',   views.pagarServicio,   name="pagarServicio"),
]