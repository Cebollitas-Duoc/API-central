from django.shortcuts import render
from rest_framework.decorators import api_view
from identificacion.decorators import *
from .validation import *
from . import procedimientos
import time

# Create your views here.

@api_view(('GET', 'POST'))
@isUserLogged()
def SendMessage(request):
    validationResult = validateSendMessage(request)
    if (not validationResult[0]):
        return Response(data={"Error": validationResult[1]})
    
    returnCode = procedimientos.sendMessage(
        request.data["SessionKey"],
        request.data["Id_Reserve"],
        int(time.time()) * 1000,
        request.data["Message"]
    )

    return Response(data={"Mensaje_Enviado": returnCode})

@api_view(('GET', 'POST'))
@isUserLogged()
def listMessages(request):
    validationResult = validateListMessages(request)
    if (not validationResult[0]):
        return Response(data={"Error": validationResult[1]})

    data = procedimientos.listMessages(
        request.data["SessionKey"],
        request.data["Id_Reserve"],
        request.data["From"]
    )

    messages = []
    if (data[1] == 1):
        for srvArray in data[0]:
            msg = {}
            msg["Id_Message"] = srvArray[0]
            msg["Id_User"]    = srvArray[1]
            msg["UserName"]   = srvArray[2]
            msg["Id_Reserve"] = srvArray[3]
            msg["Date"]       = srvArray[4]
            msg["Message"]    = srvArray[5]
            msg["Yours"]      = srvArray[6]

            messages.append(msg)
            
        return Response(data=messages)
    else:
        return Response(data={"Error": "Error interno de base de datos"})