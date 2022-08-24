from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    id_usuario = serializers.FloatField()
    password = serializers.CharField()

    class Meta:
        model = Usuario
        fields = ["id_usuario", "password"]