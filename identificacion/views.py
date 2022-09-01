from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from enum import Enum
import string
import random
from datetime import datetime, timedelta

# Create your views here.

class ReturnCodes(Enum):
    Valid = 1
    Invalid = 2

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    print("####")
    print(queryset)
    serializer_class = UsuarioSerializer
    permission_classes = []

@api_view(('GET', 'POST'))
def Login(request):
    data = {}
    if (validateLoginData(request.data) is ReturnCodes.Invalid):
        return Response(data=data)
        
    formEmail, formPassword = request.data["Email"], request.data["Password"]
    userData = userLoginData(formEmail)
    isPasswordValid = False

    if (userData["UserExist"]):
        isPasswordValid = validatePassword(formPassword, userData["Password"])
        data["Valid Password"] = isPasswordValid 
    else:
        data["ErrorCode"] = 0
        data["Error"] = "Usuario no existe"

    if (isPasswordValid):
        expirationDate = datetime.now() + timedelta(days=7)
        data["SessionKey"] = createSession(userData["ID_usuario"], expirationDate)

    return Response(data=data)

#TODO reemplazar con procedimientos almacenados
def userLoginData(email):
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
def createSession(id_Usuario, expiracion):
    data = {}
    key = generateSessionId()
    sesion = Sesion()
    sesion.id_usuario = Usuario.objects.get(id_usuario=id_Usuario)
    sesion.expiracion = expiracion
    sesion.llave = key
    data["Key"] = str(key)
    sesion.save()
    return data

def validatePassword(password, encriptedPassword):
    encriptedPassword = sparatePassword(encriptedPassword)
    algorithm = int(encriptedPassword[0])
    weight = int(encriptedPassword[1])
    salt = encriptedPassword[2]
    hash = encriptedPassword[3]

    saltedPass = password+salt
    for i in range(weight):
        newHash = calculateHash(algorithm, saltedPass+str(i))
        if (newHash == hash):
            return True
    return False

def sparatePassword(password):
    return password.split("#")

def calculateHash(algorithm, var):
    if algorithm == 1:
        return sha256(var)

def sha256(var):
    return hashlib.sha256(str(var).encode('utf-8')).hexdigest()

def validateLoginData(data):
    if ("Email" in data and "Password" in data):
        return ReturnCodes.Valid 
    return ReturnCodes.Invalid

def generateSessionId(size=64):
   return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))