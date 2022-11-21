from django.db import connection
import time

def getSessionProfile(session):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_LEE_PERFIL_DE_SESION", [session, "", "", "", "", "", 0, "", "", "", "", "", 0])
    if r[-1] == 1:
        data["Email"]     = r[1]
        data["Name"]      = r[2]
        data["Name2"]     = r[3]
        data["LastName"]  = r[4]
        data["LastName2"] = r[5]
        data["Rut"]       = r[6]
        data["Address"]   = r[7]
        data["Phone"]     = r[8]
        data["Picture"]   = r[9]
        data["Permiso"]   = r[10]

    data["ValidSession"] = r[11]
    return data

def editSessionProfile(session, email, name, name2, lastName, lastName2, rut, address, phone, id_foto):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_EDIT_SESSION_PROFILE", [session, email, name, name2, lastName, lastName2, rut, address, phone, id_foto, 0])
    return r[-1] == 1
