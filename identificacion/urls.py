from django.urls import path
from . import views

app_name = "identificacion"

urlpatterns = [
    path('Login/', views.Login, name="Login"),
    path('CreateUser/', views.CreateUser, name="CreateUser"),
]