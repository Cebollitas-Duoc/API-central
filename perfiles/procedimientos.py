from django.db import connection
import time

def getSessionProfile(session):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_LEE_PERFIL_DE_SESION", [session, "", "", "", "", "", "", "", "", "", 0])
    if r[10] == 1:
        data["Email"]     = r[1]
        data["Name"]      = r[2]
        data["Name2"]     = r[3]
        data["LastName"]  = r[4]
        data["LastName2"] = r[5]
        data["Address"]   = r[6]
        data["Phone"]     = r[7]
        data["Picture"]   = r[8]

    data["ValidSession"] = r[9]
    return data

def editSessionProfile(session, email, primernombre, segundonombre, primerapellido, segundoapellido, direccion, telefono, rutafotoperfil):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_USUARIOS.P_EDIT_SESSION_PROFILE", [session, email, primernombre, segundonombre, primerapellido, segundoapellido, direccion, telefono, rutafotoperfil, 0])
    return r[9] == 1
