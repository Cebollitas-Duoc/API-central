from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib

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
    formEmail = request.data["Email"]
    formPassword = request.data["Password"]
    userData = userLoginData(formEmail)
    data = userData
    if (userData["UserExist"]):
        data["Valid Password"] = validatePassword(formPassword, userData["password"])
    return Response(data=data)

#TODO reemplazar con procedimientos almacenados
def userLoginData(email):
    data = {}
    user = Usuario.objects.filter(email=email).first()
    if (user != None):
        data["UserExist"] = True
        data["Id"] = user.id_usuario
        data["password"] = user.password
    else:
        data["UserExist"] = False
    return data

#TODO reemplazar con procedimientos almacenados
def createSession(id_Usuario):
    data = {"test":"test UwU"}
    #data["UwU"] = request.data["testdata"]
    return Response(data=data )

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