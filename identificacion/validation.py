from ApiCentral.validateData import validateDictionary

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
        },
        "Name2" : {
            "name": "Segundo nombre",
            "type": "txt",
            "optional": True
        },
        "LastName" : {
            "name": "Apellido",
            "type": "txt",
        },
        "LastName2" : {
            "name": "Segundo apellido",
            "type": "txt",
            "optional": True
        },
        "Rut" : {
            "name": "Rut",
            "type": "rut",
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

def ValidateChangePassword(request):
    dataFormat = {
        "OldPassword" : {
            "name": "Contraseña actual",
            "type": "txt",
            "min": 5,
            "max":80            
        },
        "NewPassword" : {
            "name": "Nueva contraseña",
            "type": "txt",
            "min": 5,
            "max":80            
        },
        "NewPassword2" : {
            "name": "Validacion de la nueva contraseña",
            "type": "txt",
            "min": 5,
            "max":80,
            "sameAs": "NewPassword"
        }
    }
    
    return  validateDictionary(request.data, dataFormat)

def validateSessionKey(request):
    dataFormat = {
        "SessionKey" : {
            "name": "Llave de sesion",
            "type": "txt",          
        },
    }

    return  validateDictionary(request.data, dataFormat)

   