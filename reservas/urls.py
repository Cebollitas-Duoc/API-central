from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path('createreserve/',   views.CreateReserve,   name="CreateReserve"),
    path('getuserreserves/', views.getUserReserves, name="getUserReserves"),
    path('cancelreserve/',   views.CancelReserve,   name="CancelReserve"),
    path('addextraservice/', views.AddExtraService, name="AddExtraService"),
    path('listReserveExtraServices/<int:idReserva>/', views.listReserveExtraServices, name="listReserveExtraServices"),
    path('getreservedranges/<int:idDpto>/', views.getReservedRanges, name="getReservedRanges"),
    path('getreserveddates/<int:idDpto>/', views.getReservedDates, name="getReservedDates"),
    path('transbankpay/', views.TransbankMakePay, name="TransbankMakePay"),
    path('transbankverify/', views.TransbankVerifyPay, name="TransbankVerifyPay"),
    path('getuserreservebyid/<int:id_reserva>/', views.getReservabyId, name="getReservabyId"),
    path('listreserves/', views.listReserves, name="listReserves"),
    path('edithiredextraservicecomment/', views.editHiredExtraServiceComment, name="editHiredExtraServiceComment"),
]