from django.db import models

class TSesion(models.Model):
    id_sesion = models.FloatField(primary_key=True)
    llave = models.CharField(max_length=64, blank=True, null=True)
    expiracion = models.BigIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('TUsuario', models.DO_NOTHING, db_column='id_usuario')
    fechacreacion = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sesion'

class TPermiso(models.Model):
    id_permiso = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=4000, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_permiso'

class TEstadousuario(models.Model):
    id_estadousuario = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_estadousuario'

class TUsuario(models.Model):
    id_usuario = models.FloatField(primary_key=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    id_permiso = models.ForeignKey(TPermiso, models.DO_NOTHING, db_column='id_permiso')
    id_estadousuario = models.ForeignKey(TEstadousuario, models.DO_NOTHING, db_column='id_estadousuario')
    email = models.CharField(max_length=50, blank=True, null=True)
    primernombre = models.CharField(max_length=50, blank=True, null=True)
    segundonombre = models.CharField(max_length=50, blank=True, null=True)
    primerapellido = models.CharField(max_length=50, blank=True, null=True)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    rutafotoperfil = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_usuario'