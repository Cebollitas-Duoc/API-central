from django.urls import path
from . import views

app_name = "administracion"

urlpatterns = [
    path('viewusers/',  views.ViewUsers,  name="ViewUsers"),
    path('edituser/',   views.EditUser,   name="EditUser"),
    path('createdpto/', views.CreateDpto, name="CreateDpto"),
    path('viewdptos/',  views.ViewDptos,  name="ViewDptos"),
    path('editdptos/',  views.EditDpto,   name="EditDpto"),
]