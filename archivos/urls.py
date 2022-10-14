from django.urls import path
from . import views

app_name = "archivos"

urlpatterns = [
    path('saveimage/',  views.saveImage,  name="saveImage"),
    path('getimage/<str:imgName>/',  views.getImage,  name="getImage"),
]