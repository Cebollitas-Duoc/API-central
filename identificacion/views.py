from identificacion.sessionFunctions import hashPassword, validatePassword
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from .validation import *
from .sessionFunctions import validatePassword, hashPassword, generateRandomStr, validSession

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
        data["Valid Password"] = isPasswordValid 
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
    data["Valid"] = validSession(sessionKey)

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

#TODO reemplazar con procedimientos almacenados
def createSessionPA(id_Usuario, expiracion):
    data = {}
    key = generateRandomStr()
    sesion = Sesion()
    sesion.id_usuario = Usuario.objects.get(id_usuario=id_Usuario)
    sesion.expiracion = expiracion
    sesion.llave = key
    data["Key"] = str(key)
    sesion.save()
    return data

#TODO reemplazar con procedimientos almacenados
def CreateUserPA(email, hashedPassword, name, name2, lastName, lastName2):
    data = {}
    usuario = Usuario()
    cliente = Cliente()

    usuario.email = email
    usuario.password = hashedPassword
    usuario.id_permiso = Permiso.objects.get(id_permiso=0)
    usuario.id_estadousuario = Estadousuario.objects.get(id_estadousuario=1)
    usuario.save()

    cliente.id_usuario = usuario.id_usuario
    cliente.primerNombre = name
    cliente.segundoNombre = name2
    cliente.primerApellido = lastName
    cliente.segundoApellido = lastName2
    cliente.save()

    return data
#endregion procedimientos