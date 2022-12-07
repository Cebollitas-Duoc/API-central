from django.db import connection
import cx_Oracle

def datosgrafico():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    datos = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_GRAFICOS.P_DATOS_GRAFICO", [datos, 0])
    return (r[0], r[-1] == 1)