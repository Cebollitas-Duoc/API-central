from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path('createreserve/',  views.CreateReserve,  name="CreateReserve"),
    path('getuserreserves/',  views.getUserReserves,  name="getUserReserves"),
    path('cancelreserve/',  views.CancelReserve,  name="CancelReserve"),
]