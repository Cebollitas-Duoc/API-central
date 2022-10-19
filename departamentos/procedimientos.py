from django.db import connection
import time
import cx_Oracle


def viewDptos():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    dptos = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_DPTOS", [dptos, 0])
    return r

def viewFotosDpto(id_apartment):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    pictures = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_FOTOS_DPTO", [id_apartment, pictures, 0])
    return (r[1], r[-1] == 1)