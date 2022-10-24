from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import procedimientos
from .validation import *

# Create your views here.

@api_view(('GET', 'POST'))
def ViewDptos(request):
    data = procedimientos.viewDptos()
    dptos = []
    if (data[1] == 1):
        for usrArray in data[0]:
            usr = {}
            usr["Id_Dpto"]   = usrArray[0]
            usr["Address"]   = usrArray[1]
            usr["Longitud"]  = usrArray[2]
            usr["Latitud"]   = usrArray[3]
            usr["Rooms"]     = usrArray[4]
            usr["Bathrooms"] = usrArray[5]
            usr["Size"]      = usrArray[6]
            usr["Value"]     = usrArray[7]
            usr["Id_State"]  = usrArray[8]
            usr["Imagen"]    = usrArray[9]
                
            dptos.append(usr)
            
        return Response(data=dptos)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def ViewFotosDpto(request, idDpto):
    data = {}


    data = procedimientos.viewFotosDpto(idDpto)

    images = []
    if (data[1]):
        for imgArray in data[0]:
            img = {}
            img["Id_FotoDpto"]  = imgArray[0]
            img["Path"]         = imgArray[1]
            img["Main"]         = imgArray[2]
            img["Order"]        = imgArray[3]
                
            images.append(img)
            
        return Response(data=images)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def ViewDpto(request, idDpto):
    data = procedimientos.viewDpto(idDpto)

    if (data[1]):
        dpto = {}
        dpto["Address"]   = data[0][0]
        dpto["Longitud"]  = data[0][1]
        dpto["Latitud"]   = data[0][2]
        dpto["Rooms"]     = data[0][3]
        dpto["Bathrooms"] = data[0][4]
        dpto["Size"]      = data[0][5]
        dpto["Value"]     = data[0][6]
        dpto["Id_State"]  = data[0][7]
        dpto["Imagen"]    = data[0][8]
            
        return Response(data=dpto)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def listServices(request, idDpto):
    data = procedimientos.listServices(idDpto)
    services = []
    if (data[1] == 1):
        for srvArray in data[0]:
            srv = {}
            srv["Id_Service"]         = srvArray[0]
            srv["Id_ServiceCategory"] = srvArray[1]
            srv["Id_Estado"]          = srvArray[2]
            srv["Cantidad"]           = srvArray[3]
                
            services.append(srv)
            
        return Response(data=services)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def listServiceCategories(request):
    data = procedimientos.listServiceCategories()
    serviceCategories = []
    if (data[1] == 1):
        for catArray in data[0]:
            categorie = {}
            categorie["Id_Categoria"] = catArray[0]
            categorie["Descripcion"]  = catArray[1]
            serviceCategories.append(categorie)
            
        return Response(data=serviceCategories)
    else:
        return Response(data={"Error": "Error interno de base de datos"})
