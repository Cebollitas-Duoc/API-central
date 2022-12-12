from ApiCentral.validateData import validateDictionary

def validateSendMessage(request):
    dataFormat = {
        "Id_Reserve" : {
            "name": "Reserva",
            "type": "int"
        },
        "Message" : {
            "name": "Mensaje",
            "type": "txt",
            "max": 1000
        }
    }

    return  validateDictionary(request.data, dataFormat)

def validateListMessages(request):
    dataFormat = {
        "Id_Reserve" : {
            "name": "Reserva",
            "type": "int"
        },
        "From" : {
            "name": "Desde",
            "type": "int",
        }
    }

    return  validateDictionary(request.data, dataFormat)