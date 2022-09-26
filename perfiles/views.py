from rest_framework.decorators import api_view
from rest_framework.response import Response
from .validation import *
from identificacion.validation import validateSessionKey
import identificacion.procedimientos as authP
import identificacion.decorators as authD
import perfiles.procedimientos as procedimientos

@api_view(('GET',))
@authD.isUserLogged()
def GetSessionProfile(request):
    data = {}

    sessionKey = request.data["SessionKey"]
    data = procedimientos.getSessionProfile(sessionKey)
    return Response(data=data)

@api_view(('POST',))
def EditSessionProfile(request):
    data = {}

    validationResult = validateEditProfile(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    returnCode = procedimientos.editSessionProfile(
        request.data["SessionKey"],     
        request.data["Email"],  
        request.data["PrimerNombre"],
        request.data["SegundoNombre"],
        request.data["PrimerApellido"],
        request.data["SegundoApellido"],
        request.data["Direccion"],    
        request.data["Telefono"],          
        "",
    )
    if (not returnCode):
        data["Error"] = "No se pudo editar el perfil"
    return Response(data=data)