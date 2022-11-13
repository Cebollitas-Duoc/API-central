from identificacion.validation import isInDictionary

def validateAddReserva(request):
    data = {"Valid": True}
    if not isInDictionary("Id_Departamento", request.data):
        data["Valid"] = False
        data["Error"] = "No hay departamento"
    elif not isInDictionary("Id_Estado", request.data):
        data["Valid"] = False
        data["Error"] = "No hay estado"
    elif not isInDictionary("Valor", request.data):
        data["Valid"] = False
        data["Error"] = "No hay valor"

    return data

def validateCancelReserva(request):
    data = {"Valid": True}
    if not isInDictionary("Id_Reserva", request.data):
        data["Valid"] = False
        data["Error"] = "No hay reserva"

    return data

def validateAddExtraService(request):
    data = {"Valid": True}
    if not isInDictionary("Id_Reserve", request.data):
        data["Valid"] = False
        data["Error"] = "No hay reserva"
    elif not isInDictionary("Id_ExtSer", request.data):
        data["Valid"] = False
        data["Error"] = "No hay servicio extra"

    return data