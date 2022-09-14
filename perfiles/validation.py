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
    if not isInDictionary("PrimerNombre", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay nombre"
    if not isInDictionary("SegundoNombre", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay segundo nombre"
    if not isInDictionary("PrimerApellido", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay apellido"
    if not isInDictionary("SegundoApellido", request.data, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "No hay segundo apellido"
    
    return data