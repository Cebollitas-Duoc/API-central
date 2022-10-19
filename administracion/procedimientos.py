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

def editDpto(id_apartment, id_state, address, longitud, latitud, rooms, bathrooms, size, value):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_EDIT_DPTO", [id_apartment, id_state, address, longitud, latitud, rooms, bathrooms, size, value, 0])
    return r[-1] == 1
#endregion departamentos

#region imagen departamento

def createFotoDpto(id_apartment, main, path):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_AGREGAR_FOTO_DPTO", [id_apartment, main, path, 0])
    return r[-1] == 1

def editFotoDpto(id_imgdpto, main, order):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_EDIT_FOTO_DPTO", [id_imgdpto, main, order, 0])
    return r[-1] == 1

def deleteFotoDpto(id_imgdpto):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_ADMIN.P_BORRAR_FOTO_DPTO", [id_imgdpto, 0])
    return r[-1] == 1

#endregion imagen departamento