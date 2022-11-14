from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Residencia(models.Model):
    numero_resi = models.IntegerField(primary_key=True, unique=True, null=False, default=0)
    dueño_resi = models.CharField(max_length=30)
    telefono_resi = models.IntegerField()
    mail_resi = models.EmailField()

    def __str__(self) -> str:
        return ("Residencia N°" + str(self.numero_resi))

class Correspondencia(models.Model):
    EN_ESPERA = "En Espera a Entregar"
    ENTREGADO = "Entregado"
    NO_ENTREGADO = "No Entregado"
    ESTADO_CHOICES = [
        (EN_ESPERA, "En Espera a Entregar"),
        (ENTREGADO, "Entregado"),
        (NO_ENTREGADO, "No Entregado"),
    ]  

    fecha_recepcion = models.DateField()
    conserje = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name':"Conserje"} )
    remitente = models.CharField(max_length=30)
    destinatario = models.CharField(max_length=30)
    estado = models.CharField(choices=ESTADO_CHOICES, default=EN_ESPERA, max_length=30)
    id_residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  (str(self.id_residencia))

