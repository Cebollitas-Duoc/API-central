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
            dpto = {}
            dpto["Id_Dpto"]     = usrArray[0]
            dpto["Address"]     = usrArray[1]
            dpto["Longitud"]    = usrArray[2]
            dpto["Latitud"]     = usrArray[3]
            dpto["Rooms"]       = usrArray[4]
            dpto["Bathrooms"]   = usrArray[5]
            dpto["Size"]        = usrArray[6]
            dpto["Value"]       = usrArray[7]
            dpto["Id_State"]    = usrArray[8]
            dpto["Description"] = usrArray[9]
            dpto["Imagen"]      = usrArray[10]
                
            dptos.append(dpto)
            
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
        dpto["Address"]     = data[0][0]
        dpto["Longitud"]    = data[0][1]
        dpto["Latitud"]     = data[0][2]
        dpto["Rooms"]       = data[0][3]
        dpto["Bathrooms"]   = data[0][4]
        dpto["Size"]        = data[0][5]
        dpto["Value"]       = data[0][6]
        dpto["Id_State"]    = data[0][7]
        dpto["Description"] = data[0][8]
        dpto["Imagen"]      = data[0][9]
            
        return Response(data=dpto)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

#range services
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
#endrange services

#range extra services
@api_view(('GET', 'POST'))
def listExtraServices(request, idDpto):
    data = procedimientos.listExtraServices(idDpto)
    services = []
    if (data[1] == 1):
        for srvArray in data[0]:
            srv = {}
            srv["Id_ExtraService"] = srvArray[0]
            srv["Id_Category"]     = srvArray[1]
            srv["Id_Estado"]       = srvArray[2]
            srv["Id_Trabajador"]   = srvArray[3]
            srv["Trabajador"]      = srvArray[4]
            srv["Valor"]           = srvArray[5]
                
            services.append(srv)
            
        return Response(data=services)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def listExtraServiceCategories(request):
    data = procedimientos.listExtraServiceCategories()
    serviceCategories = []
    if (data[1] == 1):
        for catArray in data[0]:
            categorie = {}
            categorie["Id_Category"] = catArray[0]
            categorie["Description"] = catArray[1]
            serviceCategories.append(categorie)
            
        return Response(data=serviceCategories)
    else:
        return Response(data={"Error": "Error interno de base de datos"})
#endrange extraservices