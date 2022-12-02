from django.db import connection
import time
import cx_Oracle


def viewDptos():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    dptos = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_DPTO.P_LISTAR_DPTOS", [dptos, 0])
    return r

def viewDpto(id_apartment):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_DPTO.P_VER_DPTO", [id_apartment, "", 0, 0, 0, 0, 0, 0, 0, "", "", 0])
    return (r[1:-1], r[-1] == 1)

def viewFotosDpto(id_apartment):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    pictures = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_DPTO.P_LISTAR_FOTOS_DPTO", [id_apartment, pictures, 0])
    return (r[1], r[-1] == 1)

#range services
def listServices(id_apartment):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    services = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_SERVICES.P_LISTAR_SERVICES", [id_apartment, services, 0])
    return (r[1], r[-1] == 1)

def listServiceCategories():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    serviceCategories = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_SERVICES.P_LISTAR_CAT_SRV", [serviceCategories, 0])
    return (r[0], r[-1] == 1)
#endrange services

#range extra services

def listExtraServices(id_apartment):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    services = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_EXTRASERVICES.P_LIST_EXTRASERVICES", [id_apartment, services, 0])

    services = []
    if (r[-1] == 1):
        for srvArray in r[1]:
            srv = {}
            srv["Id_ExtraService"] = srvArray[0]
            srv["Id_Category"]     = srvArray[1]
            srv["Id_Estado"]       = srvArray[2]
            srv["Id_Trabajador"]   = srvArray[3]
            srv["Trabajador"]      = srvArray[4]
            srv["Valor"]           = srvArray[5]
                
            services.append(srv)

    return (services, r[-1] == 1)

def listExtraServiceCategories():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    serviceCategories = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_EXTRASERVICES.P_LIST_CAT_EXTSRV", [serviceCategories, 0])
    return (r[0], r[-1] == 1)

#endrange extra services