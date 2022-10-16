from rest_framework.decorators import api_view
from rest_framework.response import Response
import identificacion.decorators as authD
import archivos.functions as files
from .validation import *
from . import procedimientos

#region usuarios
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
                usr["Rutafotoperfil"] = ""
                
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

    imgPath = ""
    img = request.data["Imagen"]
    if (img != "undefined"):
        imgSaved, imgPath = files.saveImage(img)
    
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
        imgPath,
    )
    data["PerfilEditado"] = perfilEditado
    if (not perfilEditado):
        data["Error"] = "No se pudo editar el perfil"
    return Response(data=data)
#endregion usuarios

#region departamentos
@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def CreateDpto(request):
    data = {}
    validationResult = validateCreateDepartamento(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    returnCode = procedimientos.CreateDpto(
        request.data["IdState"],
        request.data["Address"],
        request.data["Longitud"],
        request.data["Latitud"],
        request.data["Rooms"],
        request.data["Bathrooms"],
        request.data["Size"],
        request.data["Value"],
    )

    return Response(data={"Departamento agregado": returnCode})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def ViewDptos(request):
    data = procedimientos.viewDptos()
    dptos = []
    if (data[1] == 1):
        for usrArray in data[0]:
            usr = {}
            usr["Id_Dpto"]   = usrArray[0]
            usr["Address"]   = usrArray[1]
            usr["Longitud"]  = usrArray[2]
            usr["Latitud"]   = usrArray[3]
            usr["Rooms"]     = usrArray[4]
            usr["Bathrooms"] = usrArray[5]
            usr["Size"]      = usrArray[6]
            usr["Value"]     = usrArray[7]
            usr["Id_State"]  = usrArray[8]
                
            dptos.append(usr)
            
        return Response(data=dptos)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditDpto(request):
    data = {}

    validationResult = validateEditDpto(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)
    
    dptoUpdated = procedimientos.editDpto(
        request.data["IdDpto"],
        request.data["IdState"],
        request.data["Address"],
        request.data["Longitud"],
        request.data["Latitud"],
        request.data["Rooms"],
        request.data["Bathrooms"],
        request.data["Size"],
        request.data["Value"],
    )
    data["DepartamentoEditado"] = dptoUpdated
    if (not dptoUpdated):
        data["Error"] = "No se pudo editar el departamento"
    return Response(data=data)
#endregion departamentos