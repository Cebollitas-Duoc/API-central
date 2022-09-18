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

#TODO: terminar
@api_view(('POST',))
def EditMyProfile(request):
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

    usuario = TUsuario.objects.filter(id_usuario=session.id_usuario).first()
    if (usuario == None):
        data["Error"] = "Usuario sin perfil"
        return Response(data=data)
    
    try:
        usuario.primernombre = request.data["PrimerNombre"]
        usuario.segundonombre = request.data["SegundoNombre"]
        usuario.primerapellido = request.data["PrimerApellido"]
        usuario.segundoapellido = request.data["SegundoApellido"]
        usuario.direccion = request.data["Direccion"]
        usuario.telefono = request.data["Telefono"]
        usuario.save()
        #usuario.rutafotoperfil = request.data[""] TODO:Cambiar la foto de perfil
    except:
        data["Error"] = "No se pudo editar el perfil"

    return Response(data=data)

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