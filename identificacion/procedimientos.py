from django.db import connection
from .sessionFunctions import generateRandomStr
import time
from .models import *

def userCredentials(email):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_SESION.P_USER_CREADENTIALS", [email, "", "", "", 0])
    data["UserExist"]  = r[1] == "True"
    data["ID_usuario"] = r[2]
    data["Password"]   = r[3]
    return data

def sessionCredentials(sessionKey):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_SESION.P_SESSION_CREADENTIALS", [sessionKey, "", "", "", 0])
    data["ValidSession"]  = r[1] == "True"
    data["ID_usuario"]    = r[2]
    data["Password"]      = r[3]
    return data

def createSession(id_Usuario, expiracion):
    data = {}
    key = generateRandomStr()
    epoch_time = int(time.time())
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    r = cursor.callproc("PCK_SESION.P_AGREGAR_SESION", [key, id_Usuario, expiracion, epoch_time, "", "", 0])
    data["SessionKey"] = key
    data["Nombre"] = r[4]
    data["Foto"]   = r[5]
    return data

def createUser(email, hashedPassword, name, name2, lastName, lastName2, address, phone):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_AGREGAR_USUARIO", [email, 0, 1, hashedPassword, name, name2, lastName, lastName2, address, phone, "", 0])
    returncode = r[-1] == 1
    return returncode
    
def isSessionValid(sessionKey):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_SESION.P_SESION_Valida", [sessionKey, "", 0, 0, 0])
    isValid    = r[1] == "True"
    id_usuario = r[2]
    id_permiso = r[3]

    return (isValid, id_usuario, id_permiso)

def updatePassword(id_usuario, password):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_SESION.P_UPDATE_PASSWORD", [id_usuario, password, 0])

    return r[2] == 1