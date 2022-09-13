from identificacion.validation import isInDictionary

def validateGetUserProfile(userData):
    data = {"Valid": True}
    if not isInDictionary("User", userData, invalidValue=""):
        data["Valid"] = False
        data["Error"] = "Falta id usuario en el url"
    
    return data