from django.db import connection
import time

def getSessionProfile(session):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_LEE_PERFIL_DE_SESION", [session, 0, "", "", "", "", "", 0, "", "", "", "", "", 0])
    if r[-1] == 1:
        data["IdUser"]     = r[1]
        data["Email"]      = r[2]
        data["Name"]       = r[3]
        data["Name2"]      = r[4]
        data["LastName"]   = r[5]
        data["LastName2"]  = r[6]
        data["Rut"]        = r[7]
        data["Address"]    = r[8]
        data["Phone"]      = r[9]
        data["Picture"]    = r[10]
        data["Permission"] = r[11]

    data["ValidSession"] = r[12]
    return data

def editSessionProfile(session, email, name, name2, lastName, lastName2, rut, address, phone, id_foto):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_EDIT_SESSION_PROFILE", [session, email, name, name2, lastName, lastName2, rut, address, phone, id_foto, 0])
    return r[-1] == 1
