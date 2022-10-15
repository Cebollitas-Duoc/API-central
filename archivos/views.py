from django.http import FileResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import procedimientos
import base64
import hashlib
import io

# Create your views here.

@api_view(('GET', 'POST'))
def saveImage(request):
    data = {}
    img = request.data["Image"]
    fileType, imgExtension = img.content_type.split("/")

    imgRawData = img.file.read()
    imgB64 = base64.b64encode(imgRawData).decode()

    imghash = hashlib.md5(imgB64.encode()).hexdigest()
    imgDbName = f"{imghash}.{imgExtension}"
    
    fileSaved = procedimientos.insertPicture(imgDbName, imgB64)
    data["FileSaved"] = fileSaved
    data["ImgName"] = imgDbName

    return Response(data=data)

@api_view(('GET', 'POST'))
def getImage(request, imgName):
    img = procedimientos.getPicture(imgName)
    if (not img[-1]):
        return HttpResponseNotFound("Imagen no encontrada")

    imgData = str(img[0])
    base64_img_bytes = imgData.encode('utf-8')
    imgExtension = imgName[imgName.index(".")+1:]
    f = io.BytesIO(base64.decodebytes(base64_img_bytes))
    return FileResponse(f, content_type=f"image/{imgExtension}")