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
    
    userData["Email"] = request.data["Email"]
    userData["Password"] = request.data["Password"]
    userData["Password2"] = request.data["Password2"]
    userData["Name"] = request.data["Name"]
    userData["LastName"] = request.data["LastName"]

    if not isInDictionary("Name2", userData, invalidValue=None):
        pass
        userData["Name2"] = "" 
    if not isInDictionary("LastName2", userData, invalidValue=None):
        pass
        userData["LastName2"] = ""

    print(
        userData["Email"], 
        hashPassword(userData["Password"]), 
        userData["Name"], 
        userData["Name2"], 
        userData["LastName"], 
        userData["LastName2"]  
        )

    CreateUserPA(
        userData["Email"], 
        hashPassword(userData["Password"]), 
        userData["Name"], 
        userData["Name2"], 
        userData["LastName"], 
        userData["LastName2"]  
        )
    
    return Response(data=data)

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

def validateLoginData(userData):
    data = {"Valid": True}
    if not isInDictionary("Email", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif not isInDictionary("Password", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"

    return data

def validateCreateUserData(userData):
    data = {"Valid": True}
    if not isInDictionary("Email", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif not isInDictionary("Password", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"
    elif not isInDictionary("Password2", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta La validacion de la contraseña"
    elif not isInDictionary("Name", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta el nombre"
    elif not isInDictionary("LastName", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta el primer apellido"
    elif userData["Password"] != userData["Password2"]:
        data["Valid"] = False 
        data["Error"] = "Las contraseñas no son iguales"
    
    return data

def isInDictionary(data, dic, invalidValue=None):
    if (data not in dic):
        return False
    elif (dic[data] == invalidValue):
        return False
    return True

def generateRandomStr(size=64):
   return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))

def hashPassword(password):
    algorithm = "01"
    weight = "40"
    salt = generateRandomStr(8)
    randomNumber = random.randrange(0, int(weight))
    password = f"{password}{salt}{randomNumber}"
    hashedPassword = f"{algorithm}#{weight}#{salt}#{calculateHash(algorithm, password)}"

    return hashedPassword
    