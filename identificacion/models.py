from django.db import models

# Create your models here.

class Sesion(models.Model):
    id_sesion = models.FloatField(primary_key=True)
    llave = models.CharField(max_length=64, blank=True, null=True)
    expiracion = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'sesion'

class Usuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    password = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'