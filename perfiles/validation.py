from identificacion.validation import isInDictionary

def validateGetUserProfile(userData):
    data = {"Valid": True}
    if not isInDictionary("User", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta id usuario en el url"
    
    return data

#TODO: agregar otros valores necesarios para la edicion 
#TODO: importante! los valores del formulario se encontraran dentro de equest.data y la llave de S en request.headers
def validateEditProfile(request):
    data = {"Valid": True}
    if not isInDictionary("SessionKey", request.headers, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Usuario no se encuntra logeado"
    elif not isInDictionary("Email", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay Email"
    elif not isInDictionary("PrimerNombre", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay nombre"
    elif not isInDictionary("SegundoNombre", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay segundo nombre"
    elif not isInDictionary("PrimerApellido", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay apellido"
    elif not isInDictionary("SegundoApellido", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay segundo apellido"
    elif not isInDictionary("Direccion", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay direccion"
    elif not isInDictionary("Telefono", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay telefono"

    return data