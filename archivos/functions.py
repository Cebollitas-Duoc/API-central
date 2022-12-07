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

def saveFile(file, id_category, id_reserva):
    contantType = file.content_type
    fileType, fileExtension = contantType.split("/")

    fileRawData = file.file.read()
    fileB64 = base64.b64encode(fileRawData).decode()

    filehash = hashlib.md5(fileB64.encode()).hexdigest()
    fileDbName = f"{filehash}.{fileExtension}"
    
    fileSaved = procedimientos.insertDocument(fileDbName, id_category, id_reserva, contantType, fileB64)

    return (fileSaved, fileDbName)