from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path('createreserve/',   views.CreateReserve,   name="CreateReserve"),
    path('getuserreserves/', views.getUserReserves, name="getUserReserves"),
    path('cancelreserve/',   views.CancelReserve,   name="CancelReserve"),
    path('addextraservice/', views.AddExtraService, name="AddExtraService"),
    path('listReserveExtraServices/<int:idReserva>/', views.listReserveExtraServices, name="listReserveExtraServices"),
]