from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

# Create your models here.
class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Es_activo = models.BooleanField(default=True, verbose_name="Activo")
    Fecha_de_la_orden = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la orden")

    def __str__(self):
        return f"Orden {self.id} - por: {self.usuario.username}"

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return f"{self.orden} x {self.producto} en {self.cantidad} unidades"