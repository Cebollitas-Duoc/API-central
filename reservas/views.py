from django.shortcuts import render
from rest_framework.response import Response
from identificacion import procedimientos as authProcedures
from identificacion.decorators import *
from rest_framework.decorators import api_view
from .validation import *
from . import procedimientos
from . import functions
import time

# Create your views here.

@api_view(('GET', 'POST'))
def TransbankMakePay(request):
    res = functions.TransbankMakePay(request.data["total"])
    return Response(data={"link": res})

@api_view(('GET', 'POST'))
def TransbankVerifyPay(request):
    token = request.GET.get('token_ws')
    res = functions.TransbankCommit(token)
    return Response(data={"response": res})

@api_view(('GET', 'POST'))
@isUserLogged()
def CreateReserve(request):
    data = {}
    validationResult = validateAddReserva(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    dateRange = (int(request.data["StartDate"]), int(request.data["EndDate"]))
    rangeCollides = functions.rangeColidesWithReserves( dateRange, request.data["Id_Departamento"])
    if (rangeCollides):
        return Response(data={"reserva_creada": False, "Error": "Rango de dias ya reservado"})

    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])

    price = functions.calculateReservePrice(request)
    returnCode = procedimientos.crearReserva(
        userCredentials["ID_usuario"],     
        request.data["Id_Departamento"],  
        0,
        dateRange[0],
        dateRange[1],
        int(time.time()) * 1000,
        price
    )

    if (returnCode[1]):
        if ("extraServices" in request.data):
            for extSrv in request.data["extraServices"].split(","):
                procedimientos.addExtraService(
                    returnCode[0],
                    extSrv,
                    True,
                )
    
    return Response(data={"reserva_creada": returnCode[1], "IdReserva": returnCode[0]})


@api_view(('GET', 'POST'))
@isUserLogged()
def getUserReserves(request):
    userCredentials = authProcedures.sessionCredentials(request.data["SessionKey"])


    data = procedimientos.getUserReserves(userCredentials["ID_usuario"])
    reserves = []
    if (data[1] == 1):
        for rsvArray in data[0]:
            rsv = {}
            rsv["Id_Reserve"]    = rsvArray[0]
            rsv["Id_User"]       = rsvArray[1]
            rsv["Id_Dpto"]       = rsvArray[2]
            rsv["Id_Estate"]     = rsvArray[3]
            rsv["Id_Payment"]    = rsvArray[4]
            rsv["RawStartDate"]  = rsvArray[5]
            rsv["RawEndDate"]    = rsvArray[6]
            rsv["Value"]         = rsvArray[7]
            rsv["RawCreateDate"] = rsvArray[8]

            rsv["StartDate"]  = time.strftime('%d-%m-%Y', time.gmtime(rsv["RawStartDate"]/1000))
            rsv["EndDate"]    = time.strftime('%d-%m-%Y', time.gmtime(rsv["RawEndDate"]/1000))
            rsv["CreateDate"] = time.strftime('%d-%m-%Y', time.gmtime(rsv["RawCreateDate"]/1000))
            reserves.append(rsv)
            
        return Response(data=reserves)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
@isUserLogged()
def CancelReserve(request):
    data = {}
    validationResult = validateCancelReserva(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
    
    if not ((userCredentials["ID_usuario"] == reserve[0][1]) or (userCredentials["ID_permiso"] > 0)):
        return Response(data={"Error": "Esta reserva no te pretenece"})

    data = procedimientos.listHiredExtraServices(idReserva)
    extraServices = []
    if (data[1] == 1):
        for rsvArray in data[0]:
            extSrv = {}
            extSrv["Id_HiredExtSrv"] = rsvArray[0]
            extSrv["Id_ExtSrv"]      = rsvArray[1]
            extSrv["Value"]          = rsvArray[2]
            extSrv["Included"]       = rsvArray[3]
            extSrv["Id_Payment"]     = rsvArray[4]
            extSrv["PaymentState"]   = rsvArray[5]
            extSrv["Id_Category"]    = rsvArray[6]
            extSrv["Category"]       = rsvArray[7]
            if extSrv["Included"]:
                extSrv["Estate"] = "Incluido"
            elif (extSrv["PaymentState"] == 1):
                extSrv["Estate"] = "Pagado"
            elif (extSrv["PaymentState"] == 2):
                extSrv["Estate"] = "Cancelado"
            else:
                extSrv["Estate"] = "Por pagar"
            extraServices.append(extSrv)
            
        return Response(data=extraServices)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def getReservedRanges(request, idDpto):
    data = procedimientos.getReservedRanges(idDpto)
    if (data[1] == 1):
        return Response(data=data[0])
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def getReservedDates(request, idDpto):
    data = procedimientos.getReservedRanges(idDpto)
    if (data[1] == 1):
        dates = []
        for range in data[0]:
            dates += functions.getDateRanges(range[0], range[1])
        return Response(data=dates)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
def getReservabyId(request, id_reserva):
    data = procedimientos.getReserva(id_reserva)
    if (data[1]):
        cursor                           = data[0]
        reserva = {}
        reserva["ID_RESERVA"]      = cursor[0]
        reserva["ID_USUARIO"]      = cursor[1]
        reserva["ID_DEPARTAMENTO"] = cursor[2]
        reserva["DIRECCION"]       = cursor[3]
        reserva["ID_ESTADORESERVA"]= cursor[4]
        reserva["ESTADO_RESERVA"]  = cursor[5]
        reserva["ID_PAGO"]         = cursor[6]
        reserva["ESTADO_PAGO"]     = cursor[7]
        reserva["RawFECHADESDE"]   = cursor[8]
        reserva["RawFECHAHASTA"]   = cursor[9]
        reserva["VALORTOTAL"]      = cursor[10]
        reserva["RawFECHACREACION"]= cursor[11]
        reserva["NOMBRE"]          = cursor[12]

        reserva["FECHADESDE"]    = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHADESDE"]/1000))
        reserva["FECHAHASTA"]    = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHAHASTA"]/1000))
        reserva["FECHACREACION"] = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHACREACION"]/1000)) 
        return Response(data=reserva)


@api_view(('GET', 'POST'))
@isUserLogged(permission=1)
def listReserves(request):
    data = procedimientos.listReserves()
    reserves = []
    if (data[1] == 1):
        for reserveArray in data[0]:
            reserve = {}
            reserve["Id_Reserve"]    = reserveArray[0]
            reserve["Id_User"]       = reserveArray[1]
            reserve["Id_Dpto"]       = reserveArray[2]
            reserve["Address"]       = reserveArray[3]
            reserve["Id_Estado"]     = reserveArray[4]
            reserve["Estado"]        = reserveArray[5]
            reserve["Id_Pago"]       = reserveArray[6]
            reserve["EstadoPago"]    = reserveArray[7]
            reserve["RawStartDate"]  = reserveArray[8]
            reserve["RawEndDate"]    = reserveArray[9]
            reserve["Value"]         = reserveArray[10]
            reserve["RawCreateDate"] = reserveArray[11]
            reserve["UserName"]      = reserveArray[12]

            reserve["StartDate"]  = time.strftime('%d-%m-%Y', time.gmtime(reserve["RawStartDate"]/1000))
            reserve["EndDate"]    = time.strftime('%d-%m-%Y', time.gmtime(reserve["RawEndDate"]/1000))
            reserve["CreateDate"] = time.strftime('%d-%m-%Y', time.gmtime(reserve["RawCreateDate"]/1000))
            reserves.append(reserve)
            
        return Response(data=reserves)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

