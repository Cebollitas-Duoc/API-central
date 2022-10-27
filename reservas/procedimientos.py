from django.db import connection
import time

def crearReserva(id_usr, id_dpto, id_estdo, valor):
    data = {}
    cursor = connection.cursor()
    r = cursor.callproc("PCK_RESERVA.P_CREAR_RESERVA", [id_usr, id_dpto, id_estdo, valor, 0])
    return r[-1] == 1
    