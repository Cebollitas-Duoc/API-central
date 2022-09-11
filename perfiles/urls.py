from django.urls import path
from . import views

app_name = "perfiles"

urlpatterns = [
    path('GetUserProfile/', views.GetUserProfile, name="GetUserProfile"),
    path('GetMyProfile/', views.GetMyProfile, name="GetMyProfile"),
]