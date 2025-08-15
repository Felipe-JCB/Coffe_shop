from django.urls import path
from .views import ProductoFormView, ProductoListView

urlpatterns = [
    path("agregar/", ProductoFormView.as_view(), name="agregar_producto"),
    path("listar/", ProductoListView.as_view(), name="listar_productos"),
]
