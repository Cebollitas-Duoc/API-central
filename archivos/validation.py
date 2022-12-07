from ApiCentral.validateData import validateDictionary

def validateSaveDoc(request):
    dataFormat = {
        "Document" : {
            "name": "Documento",
            "type": "txt"
        },
        "Id_Category" : {
            "name": "Categoria",
            "type": "int",
        },
        "Id_Reserve" : {
            "name": "Reserva",
            "type": "int",
        },

    }

    return  validateDictionary(request.data, dataFormat)