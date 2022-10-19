from identificacion.validation import isInDictionary

def validateViewDptoImages(request):
    data = {"Valid": True}
    if not isInDictionary("IdApartment", request.data):
        data["Valid"] = False
        data["Error"] = "No hay departamento"

    return data