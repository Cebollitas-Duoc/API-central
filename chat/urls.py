from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('sendmessage/',  views.SendMessage,  name="SendMessage"),
    path('listmessages/', views.listMessages, name="listMessages"),
]