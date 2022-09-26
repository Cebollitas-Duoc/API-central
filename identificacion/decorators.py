import identificacion.procedimientos as procedimientos
from identificacion.validation import validateSessionKey
from rest_framework.response import Response

def isUserLogged(permission=None):
    def inner(func):
        def wrapper(*args, **kw):
            data = {}
            request = (args[0])
            validationResult = validateSessionKey(request.data)
            if (not validationResult["Valid"]):
                data["Error"] = validationResult["Error"]
                return Response(data=data)

            sessionInfo = procedimientos.isSessionValid(request.data["SessionKey"]) 
            if (sessionInfo[0] and (sessionInfo[2] == permission or permission == None)):
                return func(*args, **kw)
            else:
                return Response(data={"ValidSession": False})
        return wrapper
    return inner