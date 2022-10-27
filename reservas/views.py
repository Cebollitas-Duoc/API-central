from django.shortcuts import render
from rest_framework.response import Response
from identificacion import procedimientos as authProcedures
from identificacion.decorators import *
from rest_framework.decorators import api_view
from .validation import *
from . import procedimientos

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
        request.data["Valor"],

    )
    return Response(data={"reserva_creada": returnCode})