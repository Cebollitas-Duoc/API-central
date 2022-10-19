from identificacion.validation import isInDictionary

#TODO: agregar otros valores necesarios para la edicion 
def validateEditUser(request):
    data = {"Valid": True}
    if not isInDictionary("IdUsuario", request.data):
        data["Valid"] = False
        data["Error"] = "No hay usuario"
    elif not isInDictionary("IdPermiso", request.data):
        data["Valid"] = False
        data["Error"] = "No hay permiso"
    elif not isInDictionary("IdEstado", request.data):
        data["Valid"] = False
        data["Error"] = "No hay estado"
    elif not isInDictionary("Email", request.data):
        data["Valid"] = False
        data["Error"] = "No hay Email"
    elif not isInDictionary("PrimerNombre", request.data):
        data["Valid"] = False
        data["Error"] = "No hay nombre"
    elif not isInDictionary("PrimerApellido", request.data):
        data["Valid"] = False
        data["Error"] = "No hay apellido"
    elif not isInDictionary("Direccion", request.data):
        data["Valid"] = False
        data["Error"] = "No hay direccion"
    elif not isInDictionary("Telefono", request.data):
        data["Valid"] = False
        data["Error"] = "No hay telefono"

    return data

def validateCreateDepartamento(request):
    data = {"Valid": True}
    if not isInDictionary("IdState", request.data):
        data["Valid"] = False
        data["Error"] = "No hay estado"
    elif not isInDictionary("Address", request.data):
        data["Valid"] = False
        data["Error"] = "No hay direccion"
    elif not isInDictionary("Longitud", request.data):
        data["Valid"] = False
        data["Error"] = "No hay longitud"
    elif not isInDictionary("Latitud", request.data):
        data["Valid"] = False
        data["Error"] = "No hay latitud"
    elif not isInDictionary("Rooms", request.data):
        data["Valid"] = False
        data["Error"] = "No hay habitaciones"
    elif not isInDictionary("Bathrooms", request.data):
        data["Valid"] = False
        data["Error"] = "No hay baños"
    elif not isInDictionary("Size", request.data):
        data["Valid"] = False
        data["Error"] = "No hay tamaño"
    elif not isInDictionary("Value", request.data):
        data["Valid"] = False
        data["Error"] = "No hay valor diario"
    
    return data

def validateEditDpto(request):
    if not isInDictionary("IdDpto", request.data):
        data = {
            "Valid": False,
            "Error": "No hay id del departamento"
        }
        return data

    #valida todos los datos necesarios para el departamento, solo falta la id
    validationResult = validateCreateDepartamento(request)
    if (not validationResult["Valid"]):
        return validationResult

    return {"Valid": True}


def validateAddDptoImage(request):
    data = {"Valid": True}
    if not isInDictionary("IdApartment", request.data):
        data["Valid"] = False
        data["Error"] = "No hay departamento"
    elif not isInDictionary("Main", request.data):
        data["Valid"] = False
        data["Error"] = "No se especifica si es la foto principal o no"
    elif not isInDictionary("Imagen", request.data):
        data["Valid"] = False
        data["Error"] = "No hay imagen"

    return data

def validateEditDptoImage(request):
    data = {"Valid": True}
    if not isInDictionary("IdImgDpto", request.data):
        data["Valid"] = False
        data["Error"] = "No hay imagen"
    elif not isInDictionary("Main", request.data):
        data["Valid"] = False
        data["Error"] = "No se especifica si es la foto principal o no"

    return data

def validateDeleteDptoImages(request):
    data = {"Valid": True}
    if not isInDictionary("IdDptoImg", request.data):
        data["Valid"] = False
        data["Error"] = "No hay imagen"

    return data