def isInDictionary(data, dic, invalidValue=None):
    if (data not in dic):
        return False
    elif (dic[data] == invalidValue):
        return False
    return True

def validateLoginData(userData):
    data = {"Valid": True}
    if not isInDictionary("Email", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif not isInDictionary("Password", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"

    return data
#address, phone):
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
    elif not isInDictionary("Address", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta la direccion"
    elif not isInDictionary("Phone", userData, invalidValue=""):
        data["Valid"] = False 
        data["Error"] = "Falta el telefono"
    elif userData["Password"] != userData["Password2"]:
        data["Valid"] = False 
        data["Error"] = "Las contraseñas no son iguales"
    
    return data

def validateSessionKey(requestHeaders):
    data = {"Valid": True}
    if not isInDictionary("SessionKey", requestHeaders, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Usuario no se encuntra logeado"
    
    return data