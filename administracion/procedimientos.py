from django.db import connection
import time
import cx_Oracle

def viewUsers():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    usuarios = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_USUARIOS", [usuarios, 0])
    return r

def editUser(id_usuario, id_permiso, id_estado, nombre, segundoNombre, apellido, segundoApellido, direccion, telefono, foto):
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_USUARIOS", [id_usuario, id_permiso, id_estado, nombre, segundoNombre, apellido, segundoApellido, direccion, telefono, foto, 0])
    return r[-1] == 1