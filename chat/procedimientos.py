from django.db import connection
import cx_Oracle

def sendMessage(session, id_Rsv, fecha, msg):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_CHAT.P_SUBIR_MENSAJE", [session, id_Rsv, fecha, msg, 0])
    return r[-1] == 1

def listMessages(session, id_Rsv, desde):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    mensajes = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_CHAT.P_LIST_MSG", [session, id_Rsv, desde, mensajes, 0])
    return (r[-2] , r[-1] == 1)