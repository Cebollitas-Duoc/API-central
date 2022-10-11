from django.db import connection
import time
import cx_Oracle

#region usuarios
def viewUsers():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    usuarios = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_USUARIOS", [usuarios, 0])
    return r

def editUser(id_usuario, id_permiso, id_estado, email, nombre, segundoNombre, apellido, segundoApellido, direccion, telefono, foto):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_EDIT_USER", [id_usuario, id_permiso, id_estado, email, nombre, segundoNombre, apellido, segundoApellido, direccion, telefono, foto, 0])
    return r[-1] == 1
#endregion usuarios

#region departamentos
def CreateDpto(ID_State, Address, Longitud, Latitud, Rooms, bathrooms, size, value):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_AGREGAR_DPTO", [ID_State, Address, Longitud, Latitud, Rooms, bathrooms, size, value, 0])
    return r[-1] == 1

def viewDptos():
    cursor = connection.cursor()
    raw_cursor = cursor.connection.cursor()
    dptos = raw_cursor.var(cx_Oracle.CURSOR) 
    r = cursor.callproc("PCK_ADMIN.P_LISTAR_DPTOS", [dptos, 0])
    return r

def editDpto(id_apartment, id_state, address, longitud, latitud, rooms, bathrooms, size, value):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_EDIT_DPTO", [id_apartment, id_state, address, longitud, latitud, rooms, bathrooms, size, value, 0])
    return r[-1] == 1
#endregion departamentos