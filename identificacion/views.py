import identificacion.procedimientos as procedimientos
from identificacion.sessionFunctions import hashPassword, validatePassword
from identificacion.decorators import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .validation import *
from .sessionFunctions import validatePassword, hashPassword, LoginProcess

@api_view(('GET', 'POST'))
def Login(request):
    return LoginProcess(request)

@api_view(('GET', 'POST'))
def AdminLogin(request):
    return LoginProcess(request, 1)

@api_view(('GET', 'POST'))
def CreateUser(request):
    returnInfo = {"UserCreated": False}

    validationResult = validateCreateUserData(request)
    if (not validationResult[0]):
        returnInfo["Error"] = validationResult[1]
        return Response(data=returnInfo)

    userCredentials = procedimientos.userCredentials(request.data["Email"])
    if (userCredentials["UserExist"]):
        returnInfo["Error"] = "Correo ya utilizado"
        return Response(data=returnInfo)

    returnCode = procedimientos.createUser(
        request.data["Email"], 
        hashPassword(request.data["Password"]), 
        request.data["Name"], 
        request.data.get("Name2", ""), 
        request.data["LastName"],
        request.data.get("LastName2", ""), 
        request.data["Rut"],
        request.data["Address"],
        request.data["Phone"],
        )
    
    returnInfo["UserCreated"] = returnCode

    return Response(data=returnInfo)

@api_view(('GET', 'POST'))
def ValidateSession(request):
    data = {"Valid": False}

    print(request.data)
    validationResult = validateSessionKey(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    sessionKey = request.data["SessionKey"]
    print(sessionKey)
    result = procedimientos.isSessionValid(sessionKey)
    data["Valid"] = result[0]
    data["userId"] = result[1]

    return Response(data=data)

@api_view(('GET', 'POST'))
@isUserLogged()
def ChangePassword(request):
    validationResult = ValidateChangePassword(request.data)
    if (not validationResult["Valid"]):
        return Response(data={"Error": validationResult["Error"]})
    
    sessionKey    = request.data["SessionKey"]
    old_password  = request.data["OldPassword"]
    new_password  = request.data["NewPassword"]

    userCredentials = procedimientos.sessionCredentials(sessionKey) 
    isPasswordValid = validatePassword(old_password, userCredentials["Password"])

    if (isPasswordValid):
        id_usuario = userCredentials["ID_usuario"]
        password   = hashPassword(new_password)
        returncode = procedimientos.updatePassword(id_usuario, password)
        if (returncode):
            return Response(data={"Status": "Contraseña actualizada"})
        else:
            return Response(data={"Error": "Error de base de datos"})
    else:
        return Response(data={"Error": "Contraseña incorrecta"})

