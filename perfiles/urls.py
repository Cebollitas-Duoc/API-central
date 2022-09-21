from django.urls import path
from . import views

app_name = "perfiles"

urlpatterns = [
    path('getsessionprofile/', views.GetSessionProfile, name="GetSessionProfile"),
    path('editsessionprofile/', views.EditSessionProfile, name="EditSessionProfile"),
]