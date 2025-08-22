from django.urls import path

from .views import MiOrdenView, CrearOrdenProductoView

urlpatterns = [
    path("mi-orden", MiOrdenView.as_view(), name="mi_orden"),
    path("agregar-producto", CrearOrdenProductoView.as_view(), name="agregar_producto"),
]