from django.db import models
# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    nacimiento = models.CharField(max_length=200)
    numero_documento = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.nacimiento}, {self.numero_documento}, {self.id}"