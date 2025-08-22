from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Orden
from .formularios import OrdenProductoForm


class MiOrdenView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = "ordenes/mi_orden.html"
    context_object_name = "orden"

    def get_object(self, queryset=None):
        return Orden.objects.filter(Es_activo=True, usuario=self.request.user).first()


class CrearOrdenProductoView(LoginRequiredMixin, CreateView):
    template_name = "ordenes/crear_orden_producto.html"
    form_class = OrdenProductoForm
    success_url = reverse_lazy("mi_orden")

    def form_valid(self, form):
        orden, _ = Orden.objects.get_or_create(
            Es_activo=True,
            usuario=self.request.user,
        )
        form.instance.orden = orden
        form.instance.cantidad = 1
        form.save()
        return super().form_valid(form)