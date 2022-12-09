from . import procedimientos
import base64
import hashlib
import io
import pdfkit
from django.conf import settings
from os import path
import reservas.procedimientos as rsvPro

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

    return saveEncodedFile(id_category, id_reserva, contantType, fileB64, fileExtension)

def saveEncodedFile(id_category, id_reserva, contantType, fileB64, fileExtension):
    filehash = hashlib.md5(fileB64.encode()).hexdigest()
    fileDbName = f"{filehash}.{fileExtension}"
    
    fileSaved = procedimientos.insertDocument(fileDbName, id_category, id_reserva, contantType, fileB64)

    return (fileSaved, fileDbName)

def createCheckIn(idRsv):
    html = generateCheckInDocument(idRsv)
    encodedPdf = htmlToPdf(html)
    return saveEncodedFile(1, idRsv, "application/pdf", encodedPdf, "pdf")

def htmlToPdf(html):
    pdf = pdfkit.from_string(html, False)
    encoded = str(base64.b64encode(pdf))[2:-1]
    return encoded

def generateCheckInDocument(idRsv):
    baseDir = str(settings.BASE_DIR)
    templatesPath = "archivos/templates"
    htmlPath = path.join(baseDir, templatesPath, "CheckIn.html")
    reserveData = rsvPro.getReserva(idRsv)
    html = open(htmlPath, "r").read()

    html = html.replace("*Address",   str(reserveData["DIRECCION"]))
    html = html.replace("*Rooms",     str(reserveData["ROOMS"]))
    html = html.replace("*BathRooms", str(reserveData["BATHROOMS"]))
    html = html.replace("*Services",  "POR INTEGRAR")

    html = html.replace("*Name",  str(reserveData["NOMBRE"]))
    html = html.replace("*Rut",   str(reserveData["RUT"]))
    html = html.replace("*Email", str(reserveData["EMAIL"]))
    html = html.replace("*Phone", str(reserveData["PHONE"]))

    html = html.replace("*IdReserve",  str(reserveData["ID_RESERVA"]))
    html = html.replace("*CreateDate", str(reserveData["FECHACREACION"]))
    html = html.replace("*StartDate",  str(reserveData["FECHADESDE"]))
    html = html.replace("*EndDate",    str(reserveData["FECHAHASTA"]))
    html = html.replace("*Value",      str(reserveData["VALORTOTAL"]))

    return html