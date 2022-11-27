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
            "isNull": True
        },
        "Valor" : {
            "name": "Valor",
            "type": "int"
        },
    }

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
            "isNull": True
        },
        "Valor" : {
            "name": "Valor",
            "type": "int"
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
        "IdServiceCategory" : {
            "name": "Categoria de servicio",
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
            "type": "int"
        },
        "Latitud" : {
            "name": "Latitud",
            "type": "int"
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
            "type": "int"
        },
        "Latitud" : {
            "name": "Latitud",
            "type": "int"
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
            "type": "int"
        },
        "Latitud" : {
            "name": "Latitud",
            "type": "int"
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
            "type": "float"
        },
        "Value" : {
            "name": "Valor",
            "type": "int"
        },
        "Description" : {
            "name": "Descripción",
            "type": "txt"
        }
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