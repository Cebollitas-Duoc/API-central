from django.db import models

# Create your models here.

class Sesion(models.Model):
    id_sesion = models.FloatField(primary_key=True)
    llave = models.CharField(max_length=64, blank=True, null=True)
    expiracion = models.DateField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fechacreacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesion'

class Permiso(models.Model):
    id_permiso = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=4000, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permiso'

class Estadousuario(models.Model):
    id_estadousuario = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadousuario'

class Usuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='id_permiso')
    id_estadousuario = models.ForeignKey(Estadousuario, models.DO_NOTHING, db_column='id_estadousuario')
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

