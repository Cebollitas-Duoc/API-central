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

    imgPath = None
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
        request.data["Rut"],
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

#region imagen departamento

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def CreateFotoDpto(request):
    data = {}

    validationResult = validateAddDptoImage(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    img = request.data["Imagen"]
    imgSaved, imgPath = files.saveImage(img)

    if (imgSaved):
        imagenAgregada = procedimientos.createFotoDpto(
            request.data["IdApartment"],
            request.data["Main"],
            imgPath
        )
        data["ImagenAgregada"] = imagenAgregada

    if (not imgSaved or not imagenAgregada):
        data["Error"] = "No se pudo agregar la imagen"
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def UpdateFotoDpto(request):
    data = {}

    validationResult = validateEditDptoImage(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    order = None
    if ("Order" in request.data):
        order = request.data["Order"] 

    imagenModificada = procedimientos.editFotoDpto(
        request.data["IdImgDpto"],
        request.data["Main"],
        order
    )
    data["ImagenModificada"] = imagenModificada

    if (not imagenModificada):
        data["Error"] = "No se pudo modificar la imagen"
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def DeleteFotoDpto(request):
    data = {}
    validationResult = validateDeleteDptoImages(request)
    if (not validationResult["Valid"]):
        data["Error"] = validationResult["Error"]
        return Response(data=data)

    returnCode = procedimientos.deleteFotoDpto(
        request.data["IdDptoImg"],
    )

    return Response(data={"Imagen borrada": returnCode})

#endregion imagen departamento