from django.db import connection
import cx_Oracle
import time
from rut_chile import rut_chile

def crearReserva(id_usr, id_dpto, id_estdo, fechadesde, fechahasta, fechacreacion, valor):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_CREAR_RESERVA", [id_usr, id_dpto, id_estdo, fechadesde, fechahasta, fechacreacion, valor, 0, 0])
    return (r[-2] , r[-1] == 1)
    
def getUserReserves(id_usr):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    reserves = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_GET_USR_RESERVAS", [id_usr, reserves, 0])
    return (r[1], r[-1] == 1)

def getReserva(id_reserva):
    cursor = connection.cursor()
    response = cursor.callproc("PCK_RESERVA.P_GET_RESERVA", [id_reserva, 0,0,0,"",0,"",0,"",0,0,0,0,"","",0,0,0,0,0])
    response = response[1:-1]
    reserva = {}
    reserva["ID_RESERVA"]       = response[0]
    reserva["ID_USUARIO"]       = response[1]
    reserva["ID_DEPARTAMENTO"]  = response[2]
    reserva["DIRECCION"]        = response[3]
    reserva["ID_ESTADORESERVA"] = response[4]
    reserva["ESTADO_RESERVA"]   = response[5]
    reserva["ID_PAGO"]          = response[6]
    reserva["ESTADO_PAGO"]      = response[7]
    reserva["RawFECHADESDE"]    = response[8]
    reserva["RawFECHAHASTA"]    = response[9]
    reserva["VALORTOTAL"]       = response[10]
    reserva["RawFECHACREACION"] = response[11]
    reserva["NOMBRE"]           = response[12]
    reserva["EMAIL"]            = response[13]
    reserva["PHONE"]            = response[14]
    reserva["RUT"]              = response[15]
    reserva["ROOMS"]            = response[16]
    reserva["BATHROOMS"]        = response[17]
    #formatear fechas
    reserva["FECHADESDE"]    = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHADESDE"]/1000))
    reserva["FECHAHASTA"]    = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHAHASTA"]/1000))
    reserva["FECHACREACION"] = time.strftime('%d-%m-%Y', time.gmtime(reserva["RawFECHACREACION"]/1000))
    #formatear rut
    reserva["RUT"] = str(reserva["RUT"])
    reserva["RUT"] += rut_chile.get_verification_digit(reserva["RUT"])
    reserva["RUT"] = rut_chile.format_rut_with_dots(reserva["RUT"])

    return reserva

def cancelReserva(id_reserva):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_CANCEL_RESERVA", [id_reserva, 0])
    return r[-1] == 1

def getReservedRanges(id_reserva):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    ranges = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_GET_DPTO_RANGES", [id_reserva, ranges, 0])

    ranges = []
    if (r[-1]):
        for rangeArray in r[1]:
            range = (rangeArray[0], rangeArray[1])
            ranges.append(range)

    return (ranges, r[-1] == 1)

#region extra service

def hireExtraService(id_reserva, id_extSrv, included, comment):
    included = 1 if included else 0
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_ADD_EXTRA_SRV", [id_reserva, id_extSrv, included, comment, 0])
    return r[-1] == 1

def listHiredExtraServices(id_reserva):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    hiredExtraServices = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_LIST_RESERVA_EXTSRV", [id_reserva, hiredExtraServices, 0])
    success = r[-1] == 1
    extraServices = []
    if (success):
        for rsvArray in r[1]:
            extSrv = {}
            extSrv["Id_HiredExtSrv"] = rsvArray[0]
            extSrv["Id_ExtSrv"]      = rsvArray[1]
            extSrv["Value"]          = rsvArray[2]
            extSrv["Included"]       = rsvArray[3]
            extSrv["Id_Payment"]     = rsvArray[4]
            extSrv["PaymentState"]   = rsvArray[5]
            extSrv["Id_Category"]    = rsvArray[6]
            extSrv["Category"]       = rsvArray[7]
            extSrv["Comment"]        = rsvArray[8]
            extSrv["Description"]    = rsvArray[9]
            if extSrv["Included"]:
                extSrv["Estate"] = "Incluido"
            elif (extSrv["PaymentState"] == 1):
                extSrv["Estate"] = "Pagado"
            elif (extSrv["PaymentState"] == 2):
                extSrv["Estate"] = "Cancelado"
            else:
                extSrv["Estate"] = "Por pagar"
            extraServices.append(extSrv)
            
        return extraServices
    else:
        return {"Error": "Error interno de base de datos"}

#endregion extra service

def listReserves():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    reserves = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_LIST_RESERVAS", [reserves, 0])
    return (r[0], r[-1] == 1)

def editHiredExtraServiceComment(id_extsrv, comment):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_EDIT_H_EXTSRV_COM", [id_extsrv, comment, 0])
    return r[-1] == 1