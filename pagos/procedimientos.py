from django.db import connection
import cx_Oracle

def pagarReserva(ID_PAGO, ID_ESTADOPAGO, VALOR, FECHA, ID_RESERVA):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_PAGOS.P_PAGAR_RESERVA", [ID_PAGO, ID_ESTADOPAGO, VALOR, FECHA, ID_RESERVA, 0])
    return (r[-2] , r[-1] == 1)