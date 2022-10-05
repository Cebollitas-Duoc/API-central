import hashlib, string, random
from sympy import true
from .validation import *
from rest_framework.response import Response
import identificacion.procedimientos as procedimientos
from datetime import datetime, timedelta

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
    algorithm = int(algorithm)
    if algorithm == 1:
        return sha256(var)

def sha256(var):
    return hashlib.sha256(str(var).encode('utf-8')).hexdigest()

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

def LoginProcess(request, requiredPermission=0):
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

    if (userData["ID_permiso"] < requiredPermission):
        data["Error"] = "Permisos invalidos"
        return Response(data=data)

    if (isPasswordValid):
        expirationDate = datetime.now() + timedelta(days=7)
        expirationDate = expirationDate.timestamp()
        sessionData = procedimientos.createSession(userData["ID_usuario"], expirationDate)
        data["SessionKey"] = sessionData["SessionKey"]
        data["Nombre"] = sessionData["Nombre"]
        if (sessionData["Foto"] != None):
            data["Foto"] = sessionData["Foto"]
        else:
            data["Foto"] = "/img/profiles/default.png"

    return Response(data=data)