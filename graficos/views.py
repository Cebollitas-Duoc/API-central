from django.shortcuts import render
from rest_framework.response import Response
from identificacion.decorators import *
from rest_framework.decorators import api_view
from . import procedimientos
# Create your views here.

@api_view(('GET', 'POST'))
def getdatosgraficos(request):
   
    data = procedimientos.datosgrafico()
    datopagos = []
    if (data[1] == 1):
        for pagoarray in data[0]:
            pagos = {}
            pagos["ID_ESTADOPAGO"]  = pagoarray[0]
            pagos["FECHADESDE"]     = pagoarray[1]
            pagos["FECHAHASTA"]     = pagoarray[2]
            pagos["FECHA"]          = pagoarray[3]
            datopagos.append(pagos)
            
        return Response(data=datopagos)
    else:
        return Response(data={"Error": "Error interno de base de datos"})