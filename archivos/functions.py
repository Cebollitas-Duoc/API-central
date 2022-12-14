from . import procedimientos
import base64
import hashlib
import io
import pdfkit
from django.conf import settings
from os import path
import reservas.procedimientos as rsvPro
import departamentos.procedimientos as dptoPro

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
    html = generateDocument_CheckIn(idRsv)
    encodedPdf = htmlToPdf(html)
    return saveEncodedFile(1, idRsv, "application/pdf", encodedPdf, "pdf")

def createCheckOut(idRsv):
    html = generateDocument_CheckOut(idRsv)
    encodedPdf = htmlToPdf(html)
    return saveEncodedFile(2, idRsv, "application/pdf", encodedPdf, "pdf")

def generateDocument_CheckIn(idRsv):
    baseDir = str(settings.BASE_DIR)
    templatesPath = "archivos/documentTemplates"
    htmlPath = path.join(baseDir, templatesPath, "CheckIn.html")
    reserveData = rsvPro.getReserva(idRsv)
    html = open(htmlPath, "r").read()

    html = html.replace("*Address",   str(reserveData["DIRECCION"]))
    html = html.replace("*Rooms",     str(reserveData["ROOMS"]))
    html = html.replace("*BathRooms", str(reserveData["BATHROOMS"]))
    html = html.replace("*Services",  getDptoServices(reserveData["ID_DEPARTAMENTO"]))

    html = html.replace("*Name",  str(reserveData["NOMBRE"]))
    html = html.replace("*Rut",   str(reserveData["RUT"]))
    html = html.replace("*Email", str(reserveData["EMAIL"]))
    html = html.replace("*Phone", str(reserveData["PHONE"]))

    html = html.replace("*IdReserve",     str(reserveData["ID_RESERVA"]))
    html = html.replace("*CreateDate",    str(reserveData["FECHACREACION"]))
    html = html.replace("*StartDate",     str(reserveData["FECHADESDE"]))
    html = html.replace("*EndDate",       str(reserveData["FECHAHASTA"]))
    html = html.replace("*Value",         "$" + "{:,}".format(reserveData["VALORTOTAL"]))
    html = html.replace("*ExtraServices", getTableOfHiredServices(reserveData["ID_RESERVA"]))

    return html

def generateDocument_CheckOut(idRsv):
    baseDir = str(settings.BASE_DIR)
    templatesPath = "archivos/documentTemplates"
    htmlPath = path.join(baseDir, templatesPath, "CheckOut.html")
    reserveData = rsvPro.getReserva(idRsv)
    html = open(htmlPath, "r").read()

    html = html.replace("*Address",   str(reserveData["DIRECCION"]))
    html = html.replace("*Rooms",     str(reserveData["ROOMS"]))
    html = html.replace("*BathRooms", str(reserveData["BATHROOMS"]))
    html = html.replace("*Services",  getDptoServices(reserveData["ID_DEPARTAMENTO"]))

    html = html.replace("*Name",  str(reserveData["NOMBRE"]))
    html = html.replace("*Rut",   str(reserveData["RUT"]))
    html = html.replace("*Email", str(reserveData["EMAIL"]))
    html = html.replace("*Phone", str(reserveData["PHONE"]))

    html = html.replace("*IdReserve",     str(reserveData["ID_RESERVA"]))
    html = html.replace("*CreateDate",    str(reserveData["FECHACREACION"]))
    html = html.replace("*StartDate",     str(reserveData["FECHADESDE"]))
    html = html.replace("*EndDate",       str(reserveData["FECHAHASTA"]))
    html = html.replace("*Value",         "$" + "{:,}".format(reserveData["VALORTOTAL"]))
    html = html.replace("*ExtraServices", getTableOfHiredServices(reserveData["ID_RESERVA"]))

    return html

def htmlToPdf(html):
    pdf = pdfkit.from_string(html, False)
    encoded = str(base64.b64encode(pdf))[2:-1]
    return encoded

def getDptoServices(idDpto):
    data = dptoPro.listServices(idDpto)
    services = []
    if (data[1] == 1):
        for srvArray in data[0]:     
            services.append(srvArray[2])
            
        return ", ".join(services)
    else:
        return ""

def getTableOfHiredServices(idRsv):
    services = rsvPro.listHiredExtraServices(idRsv)
    if "Error" in services:
        return ""
    if len(services) == 0:
        return ""

    rows = ""
    for service in services:
        row = f"""
            <tr>
                <td>{service["Description"]}</td>
                <td>{service["Category"]}</td>
                <td>{"$" + "{:,}".format(service["Value"])}</td>
                <td class="hiredServiceStatus">{service["Estate"]}</td>
            </tr>
        """
        rows += row

    table = f"""
        <h2>Servicios extra</h2>
        <table style="width:100%">
            <tr>
                <th>Servicio</th>
                <th>Categoria</th>
                <th>Valor</th>
                <th class="hiredServiceStatus">Estado pago</th>
            </tr>
            {rows}
        </table>
    """
    return table