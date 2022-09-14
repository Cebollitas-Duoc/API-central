from django.db import models

class Sesion(models.Model):
    id_sesion = models.FloatField(primary_key=True)
    llave = models.CharField(max_length=64, blank=True, null=True)
    expiracion = models.BigIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fechacreacion = models.BigIntegerField(blank=True, null=True)

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

class Cliente(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    primernombre = models.CharField(max_length=50, blank=True, null=True)
    segundonombre = models.CharField(max_length=50, blank=True, null=True)
    primerapellido = models.CharField(max_length=50, blank=True, null=True)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=25, blank=True, null=True)
    foto = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
