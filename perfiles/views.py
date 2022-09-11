from attr import validate
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .validation import *

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
def GetMyProfile(request):
    data = {}

    validationResult = validateSessionKey(request.headers)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    sessionKey = request.headers["Sessionkey"]
    session = Sesion.objects.filter(llave=sessionKey).first()

    if (session == None):
        data["Error"] = "Sesion invalida"
        return Response(data=data)

    profiledata = getProfileData(session.id_usuario.id_usuario, True)

    return Response(data=profiledata)

#TODO: cambiar esta uncion por un procedimiento almacenado
def getProfileData(id, validated=False):
    data = {}
    
    usuario = Usuario.objects.filter(id_usuario=id, id_estadousuario=1).first()
    cliente = Cliente.objects.filter(id_usuario=id).first()

    if (cliente == None):
        data["Error"] = "Cliente no existe"
        return data

    data["Email"] = usuario.email
    data["PrimerNombre"] = cliente.primernombre
    data["SegundoNombre"] = cliente.segundonombre
    data["PrimerApellido"] = cliente.primerapellido
    data["SegundoApellido"] = cliente.segundoapellido
    data["Foto"] = cliente.foto

    if (validated):
        data["direccion"] = cliente.direccion
        data["telefono"] = cliente.telefono

    return data