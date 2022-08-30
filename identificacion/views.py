from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import os, json


from rest_framework.response import Response
from django.conf import settings

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    print("####")
    print(queryset)
    serializer_class = UsuarioSerializer
    permission_classes = []

# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     print("####")
#     print(queryset)
#     serializer_class = UsuarioSerializer
#     permission_classes = []
    