from ApiCentral.validateData import validateDictionary

def validateAddReserva(request):
    dataFormat = {
        "Id_Departamento" : {
            "name": "Departamento",
            "type": "int"
        },
        "StartDate": {
            "name": "Fecha inicio",
            "type": "int"
        },
        "EndDate": {
            "name": "Fecha fin",
            "type": "int"
        },
        "extraServices": {
            "name": "Servicios extra",
            "type": "txt",
            "optional": True
        },
    }

    return  validateDictionary(request.data, dataFormat)

def validateCancelReserva(request):
    dataFormat = {
        "Id_Reserva" : {
            "name": "Reserva",
            "type": "int"
        },
    }

    return  validateDictionary(request.data, dataFormat)

def validateAddExtraService(request):
    dataFormat = {
        "Id_Reserva" : {
            "name": "Reserva",
            "type": "int"
        },
        "Id_ExtSer" : {
            "name": "Servicio extra",
            "type": "int"
        },
    }
    return  validateDictionary(request.data, dataFormat)