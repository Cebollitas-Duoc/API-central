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
    userData = {}
    returnInfo = {"UserCreated": False}

    validationResult = validateCreateUserData(request.data)
    if (not validationResult["Valid"]):
        returnInfo["Error"] = validationResult["Error"]
        return Response(data=returnInfo)
    
    #request.data es constante y necesitamos poder agregar unos valores en caso de que no esten
    userData = request.data

    if not isInDictionary("Name2", userData):
        userData["Name2"] = "" 
    if not isInDictionary("LastName2", userData):
        userData["LastName2"] = ""

    userCredentials = procedimientos.userCredentials(userData["Email"])
    if (userCredentials["UserExist"]):
        returnInfo["Error"] = "Correo ya utilizado"
        return Response(data=returnInfo)

    returnCode = procedimientos.createUser(
        userData["Email"], 
        hashPassword(userData["Password"]), 
        userData["Name"], 
        userData["Name2"], 
        userData["LastName"], 
        userData["LastName2"],
        userData["Address"],
        userData["Phone"],
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

