from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.TextField(max_length=200, verbose_name="Nombre")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    disponibilidad = models.BooleanField(default=True, verbose_name="Disponibilidad")
    imagen = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="Imagen"
    )

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} USD - Disponibilidad: {'Sí' if self.disponibilidad else 'No'}"
