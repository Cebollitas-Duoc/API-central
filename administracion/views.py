from rest_framework.decorators import api_view
from rest_framework.response import Response
import identificacion.decorators as authD
import identificacion.procedimientos as authP
import archivos.functions as files
import time
from .validation import *
from . import procedimientos
from departamentos import procedimientos as dptoProcedimientos
from rut_chile import rut_chile

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
            usr["Rut"]              = usrArray[8]
            usr["Direccion"]        = usrArray[9]
            usr["Telefono"]         = usrArray[10]

            usr["Rut"] = str(usr["Rut"])
            usr["Rut"] += rut_chile.get_verification_digit(usr["Rut"])
            usr["Rut"] = rut_chile.format_rut_with_dots(usr["Rut"])
            if (usrArray[11] != None):
                usr["Rutafotoperfil"] = usrArray[11]
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    imgPath = None
    img = request.data["Imagen"]
    if (img != "undefined"):
        imgSaved, imgPath = files.saveImage(img)
    
    emailCredentials = authP.userCredentials(request.data["Email"])
    if (emailCredentials["UserExist"] and (emailCredentials["ID_usuario"] != int(request.data["IdUsuario"]))):
        data["Error"] = "Correo ya utilizado"
        return Response(data=data)

    rut = request.data["Rut"]
    rut = rut.replace(".","").replace("-","")
    rut = rut[:-1]

    perfilEditado = procedimientos.editUser(
        request.data["IdUsuario"],
        request.data["IdPermiso"],
        request.data["IdEstado"],
        request.data["Email"],
        request.data["Name"],
        request.data["Name2"],
        request.data["LastName"],
        request.data["LastName2"],
        rut,
        request.data["Address"],
        request.data["Phone"],
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
        request.data["Description"],
    )

    return Response(data={"Departamento agregado": returnCode})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditDpto(request):
    data = {}

    validationResult = validateEditDpto(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
        request.data["Description"],
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
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
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    returnCode = procedimientos.deleteFotoDpto(
        request.data["IdDptoImg"],
    )

    return Response(data={"Imagen borrada": returnCode})

#endregion imagen departamento

#region servicios

#region servicios
@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def AddService(request):
    data = {}
    validationResult = validateAddService(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    currentServices = dptoProcedimientos.listServices(request.data["IdDpto"])

    if (currentServices[1]):
        for srvArray in currentServices[0]:
            if (srvArray[1] == int(request.data["IdServiceCategory"])):
                return Response(data={"Error": "Este departamento ya tiene este servicio"})
    
    returnCode = procedimientos.addService(
        request.data["IdDpto"],
        request.data["IdServiceCategory"],
    )

    return Response(data={"Servicio_Agregado": returnCode})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditService(request):
    data = {}
    validationResult = validateEditService(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)
    
    returnCode = procedimientos.editService(
        request.data["IdSrv"],
        request.data["IdEstado"],
        request.data["Cantidad"],
    )

    return Response(data={"Servicio_Modificado": returnCode})
#endregion servicios

#region servicios extra
@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def AddExtraService(request):
    data = {}
    validationResult = validateAddExtraService(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    currentServices = dptoProcedimientos.listExtraServices(request.data["IdDpto"])

    if (currentServices[1]):
        for srvArray in currentServices[0]:
            if (srvArray[1] == int(request.data["IdCategory"])):
                return Response(data={"Error": "Este departamento ya tiene este servicio extra"})
    
    returnCode = procedimientos.addExtraService(
        request.data["IdDpto"],
        request.data["IdCategory"],
        request.data["IdState"],
        request.data["IdTrabajador"],
        request.data["Valor"],
    )

    return Response(data={"ServicioExtra_Agregado": returnCode})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditExtraService(request):
    data = {}
    validationResult = validateEditExtraService(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)
    
    returnCode = procedimientos.editExtraService(
        request.data["IdExtraSrv"],
        request.data["IdState"],
        request.data["IdTrabajador"],
        request.data["Valor"],
    )

    return Response(data={"Servicio_Modificado": returnCode})
#endregion servicios extra

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def AddServiceCategory(request):
    data = {}
    validationResult = validateAddServiceCategory(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)
    
    if (request.data["IsExtra"] == "0"):
        returnCode = procedimientos.addServiceCategory(request.data["Description"])
    elif (request.data["IsExtra"] == "1"):
        returnCode = procedimientos.addExtraServiceCategory(request.data["Description"])
    else:
        data["Error"] = "Hay que especificar si es o no extra con un 1 o un 0"
        return Response(data=data)

    return Response(data={"category_added": returnCode})


#endregion servicios

#region inventario

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def AddItem(request):
    data = {}

    validationResult = validateAddItem(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.addItem(
        request.data["IdDpto"],
        request.data["Name"],
        request.data["Ammount"],
    )
    data["ObjetoAgregado"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo agregar el objeto"
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditItem(request):
    data = {}

    validationResult = validateEditItem(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.editItem(
        request.data["IdItem"],
        request.data["Name"],
        request.data["Ammount"],
    )
    data["ObjetoEditado"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo editar el objeto"
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def ListItems(request, idItem):
    data = procedimientos.listItems(idItem)
    items = []
    if (data[1] == 1):
        for usrArray in data[0]:
            item = {}
            item["Id_Item"] = usrArray[0]
            item["Name"]    = usrArray[1]
            item["Ammount"] = usrArray[2]
            item["Id_Dpto"] = usrArray[3]
                
            items.append(item)
            
        return Response(data=items)
    else:
        return Response(data={"Error": "Error interno de base de datos"})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def DeleteItem(request):
    data = {}

    validationResult = validateDeleteItem(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.deleteItem(
        request.data["IdItem"]
    )
    data["ObjetoBorrado"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo borrar el objeto"
    return Response(data=data)

#endregion inventario

#region mantenciones

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def AddMaintenance(request):
    data = {}

    validationResult = validateAddMaintenance(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.addMaintenance(
        request.data["IdCategory"],
        request.data["IdDpto"],
        request.data["Description"],
        request.data["Value"],
        request.data["StartDate"],
        request.data["EndDate"],
    )
    data["MaintenanceAgregado"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo agregar la mantencion."
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def EditMaintenance(request):
    data = {}

    validationResult = validateEditMaintenance(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.editMaintenance(
        request.data["IdMaintenance"],
        request.data["Description"],
        request.data["Value"],
        request.data["StartDate"],
        request.data["EndDate"],
    )
    data["MantencionEditada"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo editar la mantencion."
    return Response(data=data)

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def ListMaintenance(request, idDpto):
    data = procedimientos.listMaintenance(idDpto)
    items = []
    if (data[1] == 1):
        for usrArray in data[0]:
            item = {}
            item["Id_Maintenance"] = usrArray[0]
            item["Id_Cat"]         = usrArray[1]
            item["Category"]       = usrArray[2]
            item["Id_Dpto"]        = usrArray[3]
            item["Description"]    = usrArray[4]
            item["Value"]          = usrArray[5]
            item["RawStartDate"]   = usrArray[6]
            item["RawEndDate"]     = usrArray[7]
            
            item["StartDate"]   = time.strftime('%d-%m-%Y', time.gmtime(item["RawStartDate"]/1000))
            item["EndDate"]     = time.strftime('%d-%m-%Y', time.gmtime(item["RawEndDate"]/1000))
            items.append(item)
            
        return Response(data=items)
    else:
        return Response(data={"Error": "Error interno de base de datos."})

@api_view(('GET', 'POST'))
@authD.isUserLogged(permission=1)
def DeleteMaintenance(request):
    data = {}

    validationResult = validateDeleteMaintenance(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    addItem = procedimientos.deleteMaintenance(
        request.data["IdMaintenance"]
    )
    data["MantencionBorrada"] = addItem
    if (not addItem):
        data["Error"] = "No se pudo borrar la mantencion."
    return Response(data=data)

#endregion mantenciones