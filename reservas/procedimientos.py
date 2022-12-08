from django.db import connection
import cx_Oracle

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
    r = cursor.callproc("PCK_RESERVA.P_GET_RESERVA", [id_reserva, 0, 0, 0, "", 0, "", 0, "", 0, 0, 0, 0, "", 0])
    return (r[1:-1], r[-1] == 1)

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
    return (r[1], r[-1] == 1)

#endregion extra service

def listReserves():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    reserves = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_LIST_RESERVAS", [reserves, 0])
    return (r[0], r[-1] == 1)