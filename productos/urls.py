from django.urls import path
from .views import ProductoFormView, ProductoListView, ProductoListAPI

urlpatterns = [
    path("agregar/", ProductoFormView.as_view(), name="agregar_producto"),
    path("", ProductoListView.as_view(), name="listar_productos"),
    path("api/", ProductoListAPI.as_view(), name="listar_productos_api"),
]