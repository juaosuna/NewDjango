from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=300, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, null=True)
    numeroDocum = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
