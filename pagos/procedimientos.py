from django.db import connection
import cx_Oracle

def pagarReserva( ID_ESTADOPAGO, VALOR, FECHA, ID_RESERVA):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_PAGOS.P_PAGAR_RESERVA", [ ID_ESTADOPAGO, VALOR, FECHA, ID_RESERVA, 0])
    return (r[-2] , r[-1] == 1)

def Get_Id_pago(Id_reserva):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_PAGOS.P_GET_PAGO_BY_ID", [ Id_reserva, 0,  0])
    return (r[-2] , r[-1] == 1)

def pagarServicios(Id_reserva):
    cursor = connection.cursor()
    r = cursor.callproc("PCK_PAGOS.P_PAGAR_SERV_EXTRA", [ Id_reserva,  0])
    return (r[-2] , r[-1] == 1)
