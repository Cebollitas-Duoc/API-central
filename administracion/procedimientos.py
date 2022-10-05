from django.db import connection
import time
import cx_Oracle

def viewUsers():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    usuarios = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_USUARIOS", [usuarios, 0])
    return r