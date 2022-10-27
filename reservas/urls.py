from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path('createreserve/',  views.CreateReserve,  name="CreateReserve"),
]