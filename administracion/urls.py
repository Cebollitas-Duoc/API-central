from django.urls import path
from . import views

app_name = "administracion"

urlpatterns = [
    path('viewusers/', views.ViewUsers, name="ViewUsers"),
    path('edituser/', views.EditUser, name="EditUser"),
]