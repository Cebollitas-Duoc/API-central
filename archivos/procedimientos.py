from django.db import connection
import time
from .models import *
import cx_Oracle

def insertPicture(name, data):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_FILES.P_INSERT_PICTURE", [name, data, 0])
    return r[-1] == 1

def getPicture(name):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    imgdata = raw_cursor.var(cx_Oracle.CLOB) 
    r = cursor.callproc("PCK_FILES.P_GET_PICTURE", [name, imgdata, 0])
    return (r[1] ,r[-1] == 1)