from django.urls import path
from . import views

app_name = "graficos"

urlpatterns = [
    path('getdatosgraficos/',   views.getdatosgraficos,   name="getdatosgraficos"),
]