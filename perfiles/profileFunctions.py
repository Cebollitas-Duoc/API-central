def removeNone(obj):
    for key in obj:
        if (obj[key] == None):
            obj[key] = ""
    return obj
    