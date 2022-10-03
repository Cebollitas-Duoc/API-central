from identificacion.validation import isInDictionary

def validateGetUserProfile(userData):
    data = {"Valid": True}
    if not isInDictionary("User", userData):
        data["Valid"] = False
        data["Error"] = "Falta id usuario en el url"
    
    return data

#TODO: agregar otros valores necesarios para la edicion 
def validateEditProfile(request):
    data = {"Valid": True}
    if not isInDictionary("SessionKey", request.data):
        data["Valid"] = False
        data["Error"] = "Usuario no se encuntra logeado"
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