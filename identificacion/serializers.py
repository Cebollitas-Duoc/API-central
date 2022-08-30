from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    id_usuario = serializers.FloatField()
    password = serializers.CharField()
    id_permiso = serializers.CharField()
    id_estadousuario = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = Usuario
        fields = ["id_usuario", "password", "id_permiso", "id_estadousuario", "email"]