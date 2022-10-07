from rest_framework.decorators import api_view
from rest_framework.response import Response
import identificacion.decorators as authD
from .validation import *
from . import procedimientos

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def ViewUsers(request):
    data = procedimientos.viewUsers()
    users = []
    if (data[1] == 1):
        for usrArray in data[0]:
            usr = {}
            usr["Id_usuario"]       = usrArray[0]
            usr["Id_permiso"]       = usrArray[1]
            usr["Id_estadousuario"] = usrArray[2]
            usr["Email"]            = usrArray[3]
            usr["Primernombre"]     = usrArray[4]
            usr["Segundonombre"]    = usrArray[5]
            usr["Primerapellido"]   = usrArray[6]
            usr["Segundoapellido"]  = usrArray[7]
            usr["Direccion"]        = usrArray[8]
            usr["Telefono"]         = usrArray[9]
            if (usrArray[10] != None):
                usr["Rutafotoperfil"] = usrArray[10]
            else:
                usr["Rutafotoperfil"] = "/img/profiles/default.png"
                
            users.append(usr)
            
        return Response(data=users)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditUser(request):
    data = {}

    validationResult = validateEditUser(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    perfilEditado = procedimientos.editUser(
        request.data["IdUsuario"],
        request.data["IdPermiso"],
        request.data["IdEstado"],
        request.data["Email"],
        request.data["PrimerNombre"],
        request.data["SegundoNombre"],
        request.data["PrimerApellido"],
        request.data["SegundoApellido"],
        request.data["Direccion"],
        request.data["Telefono"],
        "",
    )
    data["PerfilEditado"] = perfilEditado
    if (not perfilEditado):
        data["Error"] = "No se pudo editar el perfil"
    return Response(data=data)