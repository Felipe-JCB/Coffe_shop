from django import forms
from .models import Producto


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    descripcion = forms.CharField(max_length=500, label="Descripción")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    disponibilidad = forms.BooleanField(initial=True, required=False, label="Disponibilidad")
    imagen = forms.ImageField(required=False, label="Imagen")

    def guardar(self):
        Producto.objects.create(
            nombre=self.cleaned_data["nombre"],
            descripcion=self.cleaned_data["descripcion"],
            precio=self.cleaned_data["precio"],
            disponibilidad=self.cleaned_data["disponibilidad"],
            imagen=self.cleaned_data["imagen"],
        )
