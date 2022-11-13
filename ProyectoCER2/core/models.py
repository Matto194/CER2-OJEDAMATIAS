from django.db import models

# Create your models here.

class Residencia(models.Model):
    numero_residencia = models.IntegerField(max_length=3)
    nombre_residente = models.CharField(max_length=20)
    apellido_residente = models.CharField(max_length=20)

class Correspondencia(models.Model):
    entregado = models.BooleanField()
    id_resi = models.ForeignKey('Residencia', on_delete=models.CASCADE)


