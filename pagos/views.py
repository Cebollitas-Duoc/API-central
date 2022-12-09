from django.shortcuts import render
from rest_framework.response import Response
from identificacion.decorators import *
from rest_framework.decorators import api_view
from . import procedimientos
from reservas.procedimientos import getReserva
import archivos.functions as Documentos
import time

# Create your views here.
@api_view(('GET', 'POST'))
def pagarReserva(request):
    cursor = getReserva(request.data["Id_Reserva"])

    reserva = {}
    reserva["VALORTOTAL"] = cursor["VALORTOTAL"]
    date = int(time.time()) * 1000
    dataPago = procedimientos.pagarReserva(request.data["Id_Estado_Pago"], reserva["VALORTOTAL"], date, request.data["Id_Reserva"])
    if (dataPago[1]):
        Documentos.createCheckIn(dataPago[0])
        return Response(data={"Success":"El pago ha sido guardado"})
    else:
        return Response(data={"Error":"No se pudo completar el pago de la reserva"})
