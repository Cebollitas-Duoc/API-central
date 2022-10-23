def isInDictionary(data, dic):
    if ((data not in dic) or (dic[data] == "")):
        return False
    return True

def validateLoginData(userData):
    data = {"Valid": True}
    if not isInDictionary("Email", userData):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif not isInDictionary("Password", userData):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"

    return data
#address, phone):
def validateCreateUserData(userData):
    data = {"Valid": True}
    if not isInDictionary("Email", userData):
        data["Valid"] = False
        data["Error"] = "Falta el email"
    elif not isInDictionary("Password", userData):
        data["Valid"] = False 
        data["Error"] = "Falta la contraseña"
    elif not isInDictionary("Password2", userData):
        data["Valid"] = False
        data["Error"] = "Falta La validacion de la contraseña"
    elif not isInDictionary("Name", userData):
        data["Valid"] = False 
        data["Error"] = "Falta el nombre"
    elif not isInDictionary("LastName", userData):
        data["Valid"] = False 
        data["Error"] = "Falta el primer apellido"
    elif not isInDictionary("Rut", userData):
        data["Valid"] = False 
        data["Error"] = "Falta el Rut"
    elif not isInDictionary("Address", userData):
        data["Valid"] = False 
        data["Error"] = "Falta la direccion"
    elif not isInDictionary("Phone", userData):
        data["Valid"] = False 
        data["Error"] = "Falta el telefono"
    elif userData["Password"] != userData["Password2"]:
        data["Valid"] = False 
        data["Error"] = "Las contraseñas no son iguales"
    
    return data

def validateSessionKey(dictionary):
    data = {"Valid": True}
    if not isInDictionary("SessionKey", dictionary):
        data["Valid"] = False
        data["Error"] = "Usuario no se encuntra logeado"
    
    return data

def ValidateChangePassword(dictionary):
    data = {"Valid": True}
    if not isInDictionary("OldPassword", dictionary):
        data["Valid"] = False
        data["Error"] = "Falta la vieja contraseña"
    elif not isInDictionary("NewPassword", dictionary):
        data["Valid"] = False
        data["Error"] = "Falta la nueva contraseña"
    elif not isInDictionary("NewPassword2", dictionary):
        data["Valid"] = False
        data["Error"] = "Falta la repeticion de la nueva contraseña"
    elif dictionary["NewPassword"] != dictionary["NewPassword2"]:
        data["Valid"] = False
        data["Error"] = "La repeticion de la contraseña no es igual a la ingresada"
    
    return data