from django.http import FileResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
import identificacion.decorators as authD
from . import procedimientos
from . import functions
import base64
import hashlib
import io


# Create your views here.

@authD.isUserLogged()
@api_view(('GET', 'POST'))
def saveImage(request):
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