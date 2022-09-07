from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
import string
import random
from datetime import datetime, timedelta

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    print("####")
    print(queryset)
    serializer_class = UsuarioSerializer
    permission_classes = []

@api_view(('GET', 'POST'))
def Login(request):
    data = {}
    validationResult = validateLoginData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
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

@api_view(('GET', 'POST'))
def CreateUser(request):
    data = {}
    validationResult = validateCreateUserData(request.data)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    elif isInDictionary("Name2", data, invalidValue=None):
        data["Name2"] = "" 
    elif isInDictionary("LastName2", data, invalidValue=None):
        data["LastName2"] = "" 

    CreateUser(
        data["email"], 
        data["hashedPassword"], 
        data["name"], 
        data["name2"], 
        data["lastName"], 
        data["lastName2"]  
        )
    

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

#TODO reemplazar con procedimientos almacenados
def CreateUser(email, hashedPassword, name, name2, lastName, lastName2):
    data = {}
    key = generateSessionId()
    usuario = Usuario()
    cliente = Cliente()
    cliente.id_usuario = usuario.id_usuario

    usuario.email = email
    usuario.password = hashedPassword

    cliente.primerNombre = name
    cliente.segundoNombre = name2
    cliente.primerApellido = lastName
    cliente.segundoApellido = lastName2

    usuario.save()
    cliente.save()
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
    data = {"Valid": True}
    if isInDictionary("Email", data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif isInDictionary("Password", data, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"

    return data

def validateCreateUserData(data):
    data = {"Valid": True}
    if isInDictionary("Email", data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif isInDictionary("Password", data, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"
    elif isInDictionary("Password2", data, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la repeticion de la contraseña"
    elif isInDictionary("Name", data, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta el primer nombre"
    elif isInDictionary("LastName", data, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta el primer apellido"
    
    
    return data

def isInDictionary(data, dic, invalidValue=None):
    if (data not in dic):
        return False
    elif (dic[data] == invalidValue):
        return False
    return True

def generateSessionId(size=64):
   return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))