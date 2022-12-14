from django.db import connection
import time
import cx_Oracle


#region imagenes
def insertPicture(name, contantType, data):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_FILES.P_INSERT_PICTURE", [name, contantType, data, 0])
    return r[-1] == 1

def getPicture(name):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    imgdata = raw_cursor.var(cx_Oracle.CLOB) 
    r = cursor.callproc("PCK_FILES.P_GET_PICTURE", [name, "", imgdata, 0])
    return (r[1], r[2] ,r[-1] == 1)
#endregion imagenes

#region documents
def insertDocument(name, id_category, id_reserva, contantType, data):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_FILES.P_INSERT_DOCUMENT", [name, id_category, id_reserva, contantType, data, 0])
    return r[-1] == 1

def getDocument(name):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    imgdata = raw_cursor.var(cx_Oracle.CLOB) 
    r = cursor.callproc("PCK_FILES.P_GET_DOCUMENT", [name, 0, "", 0, 0, "", imgdata, 0])
    return (r[1:-1] ,r[-1] == 1)

def listarDocs(idRsv):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    docs = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_FILES.P_GET_RSV_DOCS", [idRsv, docs, 0])
    return (r[1], r[-1] == 1)
#endregion documents

def finishReserve(id_reserva):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_Finalizar_Reserva", [id_reserva, 0])
    return r[-1] == 1