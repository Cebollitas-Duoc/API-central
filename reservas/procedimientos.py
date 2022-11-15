from django.db import connection
import cx_Oracle

def crearReserva(id_usr, id_dpto, id_estdo, fechadesde, fechahasta, valor):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_CREAR_RESERVA", [id_usr, id_dpto, id_estdo, fechadesde, fechahasta, valor, 0])
    return r[-1] == 1
    
def getUserReserves(id_usr):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    reserves = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_GET_USR_RESERVAS", [id_usr, reserves, 0])
    return (r[1], r[-1] == 1)

def getReserva(id_reserva):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_GET_RESERVA", [id_reserva, 0, 0, 0, 0, 0, 0, 0, 0])
    data["id_usr"]      = r[1]
    data["id_dpto"]     = r[2]
    data["id_state"]    = r[3]
    data["id_payment"]  = r[4]
    data["fecha_desde"] = r[5]
    data["fecha_hasta"] = r[6]
    data["valor"]       = r[7]
    return data, r[-1] == 1

def cancelReserva(id_reserva):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_CANCEL_RESERVA", [id_reserva, 0])
    return r[-1] == 1

#region extra service

def addExtraService(id_reserva, id_extSrv, included):
    included = 1 if included else 0
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_ADD_EXTRA_SRV", [id_reserva, id_extSrv, included, 0])
    return r[-1] == 1

def listHiredExtraServices(id_reserva):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    hiredExtraServices = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_RESERVA.P_LIST_RESERVA_EXTSRV", [id_reserva, hiredExtraServices, 0])
    return (r[1], r[-1] == 1)

#endregion extra service