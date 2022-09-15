from identificacion.sessionFunctions import hashPassword, validatePassword
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .validation import *
from .sessionFunctions import validatePassword, hashPassword, generateRandomStr, validSession
from django.db import connection
import time

@api_view(('GET', 'POST'))
def Login(request):
    data = {}
    validationResult = validateLoginData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
        
    formEmail, formPassword = request.data["Email"], request.data["Password"]
    userData = userLoginDataPA(formEmail)
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
        data["SessionKey"] = createSessionPA(userData["ID_usuario"], expirationDate)

    return Response(data=data)

@api_view(('GET', 'POST'))
def CreateUser(request):
    userData = {}
    data = {}

    validationResult = validateCreateUserData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    userData["Email"]     = request.data["Email"]
    userData["Password"]  = request.data["Password"]
    userData["Password2"] = request.data["Password2"]
    userData["Name"]      = request.data["Name"]
    userData["LastName"]  = request.data["LastName"]

    if not isInDictionary("Name2", userData, invalidValue=None):
        userData["Name2"] = "" 
    if not isInDictionary("LastName2", userData, invalidValue=None):
        userData["LastName2"] = ""

    CreateUserPA(
        userData["Email"], 
        hashPassword(userData["Password"]), 
        userData["Name"], 
        userData["Name2"], 
        userData["LastName"], 
        userData["LastName2"]  
        )
    
    return Response(data=data)

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

#region procedimientos
#TODO reemplazar con procedimientos almacenados
def userLoginDataPA(email):
    data = {}
    user = Usuario.objects.filter(email=email, id_estadousuario=1).first()
    if (user != None):
        data["UserExist"] = True
        data["ID_usuario"] = user.id_usuario
        data["Password"] = user.password
    else:
        data["UserExist"] = False
    return data

def createSessionPA(id_Usuario, expiracion):
    key = generateRandomStr()
    epoch_time = int(time.time())
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("PCK_SESION.P_AGREGAR_SESION", [key,expiracion,id_Usuario,epoch_time])
    return str(key)

def CreateUserPA(email, hashedPassword, name, name2, lastName, lastName2):
    data = {}
    id_permiso = Permiso.objects.get(id_permiso=0).id_permiso
    id_estadousuario = Estadousuario.objects.get(id_estadousuario=1).id_estadousuario
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("PCK_USUARIOS.P_AGREGAR_ACTUALIZAR_USUARIO", [0,email,id_permiso,id_estadousuario,hashedPassword,name, name2, lastName, lastName2])

    return data