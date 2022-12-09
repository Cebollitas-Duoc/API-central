from django.urls import path
from . import views

app_name = "archivos"

urlpatterns = [
    path('saveimage/',  views.SaveImage,  name="saveImage"),
    path('getimage/<str:imgName>/',  views.getImage,  name="getImage"),
    
    path('savedoc/',  views.SaveDoc,  name="SaveDoc"),
    path('getdoc/<str:fileName>/',  views.getDoc,  name="getDoc"),
    path('listdocs/<int:idRsv>/',  views.ListDocs,  name="ListDocs"),

    path('createcheckout/<int:idRsv>/',  views.CreateCheckOut,  name="CreateCheckOut"),
    
    path('test/',  views.test,  name="test"),
]