from django.urls import path
from . import views

app_name = "identificacion"

urlpatterns = [
    path('Login/', views.Login, name="Login"),
    path('AdminLogin/', views.AdminLogin, name="AdminLogin"),
    path('CreateUser/', views.CreateUser, name="CreateUser"),
    path('ValidateSession/', views.ValidateSession, name="ValidateSession"),
    path('changepassword/', views.ChangePassword, name="ChangePassword"),
]