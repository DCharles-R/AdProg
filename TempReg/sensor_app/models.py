from django.db import models

# Create your models here.
class Lectura(models.Model):
    fecha = models.DateTimeField()
    valor = models.FloatField()
    ubicacion = models.CharField()

    def __str__(self):
        return f"{self.fecha} {self.valor} {self.ubicacion}"
