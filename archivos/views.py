from django.http import FileResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from identificacion.decorators import *
from .validation import *
from . import procedimientos
from . import functions
import base64
import hashlib
import io

#region imagenes
@api_view(('GET', 'POST'))
@isUserLogged()
def SaveImage(request):
    data = {}
    img = request.data["Image"]

    data["FileSaved"], data["ImgName"] = functions.saveImage(img)

    return Response(data=data)

@api_view(('GET', 'POST'))
def getImage(request, imgName):
    img = procedimientos.getPicture(imgName)
    if (not img[-1]):
        return HttpResponseNotFound("Imagen no encontrada")

    contantType = str(img[0])
    imgData = str(img[1])
    base64_img_bytes = imgData.encode('utf-8')
    f = io.BytesIO(base64.decodebytes(base64_img_bytes))
    return FileResponse(f, content_type=contantType)
#endregion imagenes

#region documentos
@api_view(('GET', 'POST'))
@isUserLogged()
def SaveDoc(request):
    data = {}
    
    validationResult = validateSaveDoc(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    
    file = request.data["Document"]
    idCategory = request.data["Id_Category"]
    idReserve  = request.data["Id_Reserve"]

    data["FileSaved"], data["FileName"] = functions.saveFile(file, idCategory, idReserve)

    return Response(data=data)

@api_view(('GET', 'POST'))
def getDoc(request, fileName):
    file = procedimientos.getDocument(fileName)
    if (not file[-1]):
        return HttpResponseNotFound("Documento no encontrado")
    file = file[0]

    idCat       = file[0]
    cat         = file[1]
    idRsv       = file[2]
    idUsr       = file[3]
    contantType = str(file[4])
    fileData    = str(file[5])
    base64_img_bytes = fileData.encode('utf-8')
    f = io.BytesIO(base64.decodebytes(base64_img_bytes))
    return FileResponse(f, content_type=contantType)

@api_view(('GET', 'POST'))
@isUserLogged()
def ListDocs(request, idRsv):
    data = procedimientos.listarDocs(idRsv)
    docs = []
    if (data[1] == 1):
        for docArray in data[0]:
            doc = {}
            doc["Id_Document"] = docArray[0]
            doc["Id_Category"] = docArray[1]
            doc["Category"]    = docArray[2]
            doc["ContentType"] = docArray[3]

            docs.append(doc)
            
        return Response(data=docs)
    else:
        return Response(data={"Error": "Error interno de base de datos"})
#endregion documentos

@api_view(('GET', 'POST'))
def test(request):
    idRsv = 1
    return Response(data={functions.createCheckIn(idRsv)})
