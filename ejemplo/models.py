from django.db import models

# Create your models here.
class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    numero_registro = models.IntegerField()
    
def __str__(self):
      return f"{self.nombre}, {self.tipo}, {self.direccion}, {self.id}"