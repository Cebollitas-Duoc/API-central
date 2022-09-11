from django.urls import path
from . import views

app_name = "perfiles"

urlpatterns = [
    path('UserProfile/', views.UserProfile, name="UserProfile"),
]