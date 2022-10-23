from . import procedimientos
import base64
import hashlib
import io

def saveImage(img):
    contantType = img.content_type
    fileType, imgExtension = contantType.split("/")

    imgRawData = img.file.read()
    imgB64 = base64.b64encode(imgRawData).decode()

    imghash = hashlib.md5(imgB64.encode()).hexdigest()
    imgDbName = f"{imghash}.{imgExtension}"
    
    fileSaved = procedimientos.insertPicture(imgDbName, contantType, imgB64)

    return (fileSaved, imgDbName)