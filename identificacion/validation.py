from ApiCentral.validateData import validateDictionary

def isInDictionary(data, dic):
    if ((data not in dic) or (dic[data] == "")):
        return False
    return True

def validateLoginData(request):
    dataFormat = {
        "Email" : {
            "name": "Correo",
            "type": "email",
            "min": 10
        },
        "Password" : {
            "name": "Contraseña",
            "type": "txt",
            "min": 5
        }
    }

    return  validateDictionary(request.data, dataFormat)

#address, phone):
def validateCreateUserData(request):
    dataFormat = {
        "Email" : {
            "name": "Correo",
            "type": "email",
            "min": 10
        },
        "Password" : {
            "name": "Contraseña",
            "type": "txt",
            "min": 5
        },
        "Password2" : {
            "name": "Validacion de la contraseña",
            "type": "txt",
            "min": 5,
            "sameAs": "Password"
        },
        "Name" : {
            "name": "Nombre",
            "type": "txt",
            "min": 5
        },
        "Name2" : {
            "name": "Segundo nombre",
            "type": "txt",
            "min": 5,
            "isNull": True
        },
        "LastName" : {
            "name": "Apellido",
            "type": "txt",
            "min": 5
        },
        "LastName2" : {
            "name": "Segundo apellido",
            "type": "txt",
            "min": 5,
            "isNull": True
        },
        "Rut" : {
            "name": "Rut",
            "type": "txt",
            "min": 5
        },
        "Address" : {
            "name": "Direccion",
            "type": "txt",
            "min": 5
        },
        "Phone" : {
            "name": "Numero de telefono",
            "type": "int",
            "min": 8
        },
    }

    return  validateDictionary(request.data, dataFormat)

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