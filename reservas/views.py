from django.shortcuts import render
from rest_framework.response import Response
from identificacion import procedimientos as authProcedures
from identificacion.decorators import *
from rest_framework.decorators import api_view
from .validation import *
from . import procedimientos
from . import functions

# Create your views here.

@api_view(('GET', 'POST'))
@isUserLogged()
def CreateReserve(request):
    data = {}
    validationResult = validateAddReserva(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])

    returnCode = procedimientos.crearReserva(
        userCredentials["ID_usuario"],     
        request.data["Id_Departamento"],  
        request.data["Id_Estado"],
        request.data["FechaDesde"],
        request.data["FechaHasta"],
        request.data["Valor"],
    )
    return Response(data={"reserva_creada": returnCode})

@api_view(('GET', 'POST'))
@isUserLogged()
def getUserReserves(request):
    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])

    data = procedimientos.getUserReserves(userCredentials["ID_usuario"])
    reserves = []
    if (data[1] == 1):
        for rsvArray in data[0]:
            rsv = {}
            rsv["Id_Reserva"]       = rsvArray[0]
            rsv["Id_Usuario"]       = rsvArray[1]
            rsv["Id_Departamento"]  = rsvArray[2]
            rsv["Id_Estado"]        = rsvArray[3]
            rsv["Id_Pago"]          = rsvArray[4]
            rsv["Fecha_Desde"]      = rsvArray[5]
            rsv["Fecha_Hasta"]      = rsvArray[6]
            rsv["Fecha_Valor"]      = rsvArray[7]
            reserves.append(rsv)
            
        return Response(data=reserves)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
@isUserLogged()
def CancelReserve(request):
    data = {}
    validationResult = validateCancelReserva(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])
    reserve = procedimientos.getReserva(request.data["Id_Reserva"])
    if not reserve[1]:
        return Response(data={"Error": "Error interno de base de datos"})
    
    if userCredentials["ID_usuario"] != reserve[0]["id_usr"]:
        return Response(data={"Error": "Esta reserva no te pretenece"})

    returnCode = procedimientos.cancelReserva(
        request.data["Id_Reserva"]
    )
    return Response(data={"reserva_cancelada": returnCode})


@api_view(('GET', 'POST'))
@isUserLogged()
def AddExtraService(request):
    data = {}
    validationResult = validateAddExtraService(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])
    reserve = procedimientos.getReserva(request.data["Id_Reserve"])
    if not reserve[1]:
        return Response(data={"Error": "Error interno de base de datos"})
    
    if userCredentials["ID_usuario"] != reserve[0]["id_usr"]:
        return Response(data={"Error": "Esta reserva no te pretenece"})

    returnCode = procedimientos.addExtraService(
        request.data["Id_Reserve"],
        request.data["Id_ExtSer"],
        False,
    )
    return Response(data={"servicioExtra_agregado": returnCode})

@api_view(('GET', 'POST'))
@isUserLogged()
def listReserveExtraServices(request, idReserva):
    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])
    reserve = procedimientos.getReserva(idReserva)
    if not reserve[1]:
        return Response(data={"Error": "Error interno de base de datos"})
    
    if userCredentials["ID_usuario"] != reserve[0]["id_usr"]:
        return Response(data={"Error": "Esta reserva no te pretenece"})

    data = procedimientos.listHiredExtraServices(idReserva)
    extraServices = []
    if (data[1] == 1):
        for rsvArray in data[0]:
            extSrv = {}
            extSrv["Id_HiredExtSrv"] = rsvArray[0]
            extSrv["Id_Reserve"]     = rsvArray[1]
            extSrv["Id_HiredExtSrv"] = rsvArray[2]
            extSrv["Value"]          = rsvArray[3]
            extSrv["Id_Pago"]        = rsvArray[4]
            extSrv["Included"]       = rsvArray[5]
            extraServices.append(extSrv)
            
        return Response(data=extraServices)
    else:
        return Response(data={"Error": "Error interno de base de datos"})