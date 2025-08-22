from django.forms import ModelForm
from .models import OrdenProducto


class OrdenProductoForm(ModelForm):
    class Meta:
        model = OrdenProducto
        fields = ["producto"]