from ApiCentral.validateData import validateDictionary

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
        },
        "Name2" : {
            "name": "Segundo nombre",
            "type": "txt",
            "isNull": True
        },
        "LastName" : {
            "name": "Apellido",
            "type": "txt",
        },
        "LastName2" : {
            "name": "Segundo apellido",
            "type": "txt",
            "isNull": True
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