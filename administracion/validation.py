from ApiCentral.validateData import validateDictionary

def validateEditExtraService(request):
    dataFormat = {
        "IdExtraSrv" : {
            "name": "Servicio extra",
            "type": "int"
        },
        "IdState" : {
            "name": "Estado",
            "type": "int"
        },
        "IdTrabajador" : {
            "name": "Trabajador",
            "type": "int",
            "optional": True
        },
        "Valor" : {
            "name": "Valor",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt",
            "max": 100
        },
    }

    return  validateDictionary(request.data, dataFormat)

def validateAddExtraService(request):
    dataFormat = {
        "IdDpto" : {
            "name": "Departamento",
            "type": "int"
        },
        "IdCategory" : {
            "name": "Categoria",
            "type": "int"
        },
        "IdState" : {
            "name": "Estado",
            "type": "int"
        },
        "IdTrabajador" : {
            "name": "Trabajador",
            "type": "int",
            "optional": True
        },
        "Valor" : {
            "name": "Valor",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt",
            "max": 100
        },
    }
    return  validateDictionary(request.data, dataFormat)
    
def validateEditService(request):
    dataFormat = {
        "IdSrv" : {
            "name": "Servicio",
            "type": "int"
        },
        "IdEstado" : {
            "name": "Estado",
            "type": "int"
        },
        "Cantidad" : {
            "name": "Cantidad",
            "type": "int"
        },
    }
    return  validateDictionary(request.data, dataFormat)
    
def validateAddService(request):
    dataFormat = {
        "IdDpto" : {
            "name": "Departamento",
            "type": "int"
        },
        "IdCategory" : {
            "name": "Categoria de servicio",
            "type": "int"
        },
        "IdState" : {
            "name": "Estado",
            "type": "int"
        },
        "Ammount" : {
            "name": "Cantidad",
            "type": "int"
        },
    }
    return  validateDictionary(request.data, dataFormat)

def validateDeleteDptoImages(request):
    dataFormat = {
        "IdDptoImg" : {
            "name": "Imagen Departamento",
            "type": "int"
        },
    }
    return  validateDictionary(request.data, dataFormat)

def validateEditDptoImage(request):
    dataFormat = {
        "IdImgDpto" : {
            "name": "Imagen de departamento",
            "type": "int"
        },
        "Main" : {
            "name": "Imagen principal",
            "type": "int"
        },
    }
    return  validateDictionary(request.data, dataFormat)    

def validateAddDptoImage(request):
    dataFormat = {
        "IdApartment" : {
            "name": "Departamento",
            "type": "int"
        },
        "Main" : {
            "name": "Imagen principal",
            "type": "int"
        },
        "Imagen" : {
            "name": "Imagen",
            "type": "txt"
        },
    }
    return  validateDictionary(request.data, dataFormat)

def validateEditDpto(request):
    dataFormat = {
        "IdDpto" : {
            "name": "Imagen Departamento",
            "type": "int"
        },
         "IdState" : {
            "name": "Estado",
            "type": "int"
        },
        "Address" : {
            "name": "Direccion",
            "type": "txt"
        },
        "Longitud" : {
            "name": "Longitud",
            "type": "float"
        },
        "Latitud" : {
            "name": "Latitud",
            "type": "float"
        },
        "Rooms" : {
            "name": "Habitaciones",
            "type": "int"
        },
        "Bathrooms" : {
            "name": "Baños",
            "type": "int"
        },
        "Size" : {
            "name": "Tamaño",
            "type": "int"
        },
        "Value" : {
            "name": "Valor",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt"
        },
    }
    return  validateDictionary(request.data, dataFormat)

def validateCreateDepartamento(request):
    dataFormat = {
        "IdState" : {
            "name": "Estado",
            "type": "int"
        },
        "Address" : {
            "name": "Direccion",
            "type": "txt"
        },
        "Longitud" : {
            "name": "Longitud",
            "type": "float"
        },
        "Latitud" : {
            "name": "Latitud",
            "type": "float"
        },
        "Rooms" : {
            "name": "Habitaciones",
            "type": "int"
        },
        "Bathrooms" : {
            "name": "Baños",
            "type": "int"
        },
        "Size" : {
            "name": "Tamaño",
            "type": "int"
        },
        "Value" : {
            "name": "Valor",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt"
        },
    }
    return  validateDictionary(request.data, dataFormat)

def validateAddItem(request):
    dataFormat = {
        "IdDpto" : {
            "name": "Departamento",
            "type": "int"
        },
        "Name" : {
            "name": "Nombre",
            "type": "txt"
        },
        "Ammount" : {
            "name": "Cantidad",
            "type": "int"
        }
    }

    return  validateDictionary(request.data, dataFormat)

def validateEditItem(request):
    dataFormat = {
        "IdItem" : {
            "name": "Objeto",
            "type": "int"
        },
        "Name" : {
            "name": "Nombre",
            "type": "txt"
        },
        "Ammount" : {
            "name": "Cantidad",
            "type": "int"
        }
    }

    return  validateDictionary(request.data, dataFormat)

def validateDeleteItem(request):
    dataFormat = {
        "IdItem" : {
            "name": "Objeto",
            "type": "int"
        }
    }

    return  validateDictionary(request.data, dataFormat)

def validateEditUser(request):
    dataFormat = {
        "Email" : {
            "name": "Correo",
            "type": "email",
            "min": 10
        },
        "Name" : {
            "name": "Nombre",
            "type": "txt",
        },
        "Name2" : {
            "name": "Segundo nombre",
            "type": "txt",
            "optional": True
        },
        "LastName" : {
            "name": "Apellido",
            "type": "txt",
        },
        "LastName2" : {
            "name": "Segundo apellido",
            "type": "txt",
            "optional": True
        },
        "Rut" : {
            "name": "Rut",
            "type": "rut",
        },
        "Address" : {
            "name": "Direccion",
            "type": "txt",
            "min": 5
        },
        "Phone" : {
            "name": "Numero de telefono",
            "type": "int",
            "min": 8
        },
    }

    return  validateDictionary(request.data, dataFormat)

def validateAddServiceCategory(request):
    dataFormat = {
        "Description" : {
            "name": "Descripcion",
            "type": "txt"
        },
        "IsExtra" : {
            "name": "Tipo",
            "type": "int"
        }
    }

    return  validateDictionary(request.data, dataFormat)

#region mantencion

def validateAddMaintenance(request):
    dataFormat = {
        "IdCategory" : {
            "name": "Categoria",
            "type": "int"
        },
        "IdDpto" : {
            "name": "Departamento",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt",
            "max": 200
        },
        "Value" : {
            "name": "Valor",
            "type": "int"
        },
        "StartDate" : {
            "name": "Fecha de inicio",
            "type": "int"
        },
        "EndDate" : {
            "name": "Fecha de fin",
            "type": "int"
        },
        
    }

    return  validateDictionary(request.data, dataFormat)

def validateEditMaintenance(request):
    dataFormat = {
        "IdMaintenance" : {
            "name": "Mantencion",
            "type": "int"
        },
        "Description" : {
            "name": "Descripcion",
            "type": "txt",
            "max": 200
        },
        "Value" : {
            "name": "Valor",
            "type": "int"
        },
        "StartDate" : {
            "name": "Fecha de inicio",
            "type": "int"
        },
        "EndDate" : {
            "name": "Fecha de fin",
            "type": "int"
        },
        
    }

    return  validateDictionary(request.data, dataFormat)

def validateDeleteMaintenance(request):
    dataFormat = {
        "IdMaintenance" : {
            "name": "Mantencion",
            "type": "int"
        }
    }

    return  validateDictionary(request.data, dataFormat)

#endregion mantencion