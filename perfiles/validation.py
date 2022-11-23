from identificacion.validation import isInDictionary
from ApiCentral.validateData import validateDictionary


#TODO: agregar otros valores necesarios para la edicion 
def validateEditProfile(request):
    dataFormat = {
        "Email" : {
            "name": "Correo",
            "type": "email",
            "min": 10
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
            "type": "rut",
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