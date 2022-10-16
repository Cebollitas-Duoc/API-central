from . import procedimientos
import base64
import hashlib
import io

def saveImage(img):
    fileType, imgExtension = img.content_type.split("/")

    imgRawData = img.file.read()
    imgB64 = base64.b64encode(imgRawData).decode()

    imghash = hashlib.md5(imgB64.encode()).hexdigest()
    imgDbName = f"{imghash}.{imgExtension}"
    
    fileSaved = procedimientos.insertPicture(imgDbName, imgB64)

    return (fileSaved, imgDbName)