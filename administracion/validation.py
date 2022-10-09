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