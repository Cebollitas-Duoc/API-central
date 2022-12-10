from django.shortcuts import render
from rest_framework.response import Response
from identificacion.decorators import *
from rest_framework.decorators import api_view
from . import procedimientos
import time
# Create your views here.

@api_view(('GET', 'POST'))
def getdatosgraficos(request):
   
    data = procedimientos.datosgrafico()
    datopagos = []
    if (data[1] == 1):
        for pagoarray in data[0]:
            pagos = {}
            pagos["ID_PAGO"]            = pagoarray[0]   
            pagos["ID_ESTADOPAGO"]      = pagoarray[1]
            pagos["rawFECHADESDE"]      = pagoarray[2]
            pagos["rawFECHAHASTA"]      = pagoarray[3]
            pagos["rawFECHAPAGO"]       = pagoarray[4]
            pagos["rawFECHACREACION"]   = pagoarray[5]    
            pagos["FECHADESDE"]         = time.strftime('%d-%m-%Y', time.gmtime(pagos["rawFECHADESDE"]/1000))
            pagos["FECHAHASTA"]         = time.strftime('%d-%m-%Y', time.gmtime(pagos["rawFECHAHASTA"]/1000))
            pagos["FECHAPAGO"]          = time.strftime('%d-%m-%Y', time.gmtime(pagos["rawFECHAPAGO"]/1000))
            pagos["FECHACREACION"]      = time.strftime('%d-%m-%Y', time.gmtime(pagos["rawFECHACREACION"]/1000))
            datopagos.append(pagos)
            
        return Response(data=datopagos)
    else:
        return Response(data={"Error": "Error interno de base de datos"})