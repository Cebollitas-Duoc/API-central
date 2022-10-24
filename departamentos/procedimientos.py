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