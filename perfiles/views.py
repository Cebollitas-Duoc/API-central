from requests import session
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .validation import *
from identificacion.validation import validateSessionKey
import perfiles.procedimientos as procedimientos

@api_view(('GET',))
def GetUserProfile(request):
    data = {}

    validationResult = validateGetUserProfile(request.GET)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    profiledata = getProfileData(request.GET["User"])

    return Response(data=profiledata)

@api_view(('GET',))
def GetSessionProfile(request):
    validationResult = validateSessionKey(request.headers)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    sessionKey = request.headers["Sessionkey"]
    data = procedimientos.getSessionProfile(sessionKey)
    return Response(data=data)

@api_view(('POST',))
def EditSessionProfile(request):
    data = {}

    validationResult = validateEditProfile(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    sessionKey = request.headers["Sessionkey"]
    session = TSesion.objects.filter(llave=sessionKey).first()

    if (session == None):
        data["Error"] = "Sesion invalida"
        return Response(data=data)

    returnCode = procedimientos.editSessionProfile(
        request.headers["SessionKey"],     
        request.data["Email"],  
        request.data["PrimerNombre"],
        request.data["SegundoNombre"],
        request.data["PrimerApellido"],
        request.data["SegundoApellido"],
        request.data["Direccion"],    
        request.data["Telefono"],          
        "",
    )

    return Response(data=returnCode)

    

#TODO: cambiar esta uncion por un procedimiento almacenado
def getProfileData(id, validated=False):
    data = {}
    
    usuario = TUsuario.objects.filter(id_usuario=id, id_estadousuario=1).first()

    if (usuario == None):
        data["Error"] = "Usuario no existe"
        return data

    data["Email"] = usuario.email
    data["PrimerNombre"] = usuario.primernombre
    data["SegundoNombre"] = usuario.segundonombre
    data["PrimerApellido"] = usuario.primerapellido
    data["SegundoApellido"] = usuario.segundoapellido
    data["Foto"] = usuario.foto

    if (validated):
        data["direccion"] = usuario.direccion
        data["telefono"] = usuario.telefono

    return data