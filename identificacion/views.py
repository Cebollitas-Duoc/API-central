import identificacion.procedimientos as procedimientos
from http import client
from identificacion.sessionFunctions import hashPassword, validatePassword
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .validation import *
from .sessionFunctions import validatePassword, hashPassword, validSession



@api_view(('GET', 'POST'))
def Login(request):
    data = {}
    validationResult = validateLoginData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
        
    formEmail, formPassword = request.data["Email"], request.data["Password"]
    userData = procedimientos.userCredentials(formEmail)
    isPasswordValid = False

    if (userData["UserExist"]):
        isPasswordValid = validatePassword(formPassword, userData["Password"])
        data["ValidPassword"] = isPasswordValid
    else:
        data["ErrorCode"] = 0
        data["Error"] = "Usuario no existe"

    if (isPasswordValid):
        expirationDate = datetime.now() + timedelta(days=7)
        expirationDate = expirationDate.timestamp()
        data["SessionKey"] = procedimientos.createSession(userData["ID_usuario"], expirationDate)
        #data["Nombre"] = userData["Nombre"]   
        #data["Foto"] = userData["Foto"]    

    return Response(data=data)

@api_view(('GET', 'POST'))
def CreateUser(request):
    userData = {}
    data = {}

    validationResult = validateCreateUserData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    #request.data es constante y necesitamos poder agregar unos valores en caso de que no esten
    userData = request.data

    if not isInDictionary("Name2", userData, invalidValue=None):
        userData["Name2"] = "" 
    if not isInDictionary("LastName2", userData, invalidValue=None):
        userData["LastName2"] = ""

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
    
    return Response(data=returnCode)

@api_view(('GET', 'POST'))
def ValidateSession(request):
    data = {"Valid": False}

    validationResult = validateSessionKey(request.headers)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    sessionKey = request.headers["Sessionkey"]
    result = validSession(sessionKey)
    data["Valid"] = result[0]
    data["userId"] = result[1]

    return Response(data=data)


