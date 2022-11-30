from rest_framework.decorators import api_view
from rest_framework.response import Response
from .validation import *
import identificacion.procedimientos as authP
import identificacion.decorators as authD
import archivos.functions as files
from . import procedimientos
from .functions import removeNone
from rut_chile import rut_chile

@api_view(('GET',))
@authD.isUserLogged()
def GetSessionProfile(request):
    sessionKey = request.data["SessionKey"]
    data = procedimientos.getSessionProfile(sessionKey)
    data["Rut"] = str(data["Rut"])
    data["Rut"] += rut_chile.get_verification_digit(data["Rut"])
    data["Rut"] = rut_chile.format_rut_with_dots(data["Rut"])
    return Response(data=removeNone(data))

@api_view(('POST',))
@authD.isUserLogged()
def EditSessionProfile(request):
    data = {}

    validationResult = validateEditProfile(request)
    if (not validationResult[0]):
        data["Error"] = validationResult[1]
        return Response(data=data)

    imgPath = ""
    img = request.data["Image"]
    if (img != "undefined"):
        imgSaved, imgPath = files.saveImage(img)

    userCredentials = authP.userCredentials(request.data["Email"])
    if (userCredentials["UserExist"]):
        data["Error"] = "Correo ya utilizado"
        return Response(data=data)

    rut = request.data["Rut"]
    rut = rut.replace(".","").replace("-","")
    rut = rut[:-1]

    returnCode = procedimientos.editSessionProfile(
        request.data["SessionKey"],     
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
    if (not returnCode):
        data["Error"] = "No se pudo editar el perfil"
    return Response(data=data)