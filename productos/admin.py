from django.contrib import admin
from .models import Producto
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ["marca", "nombre", "precio", "disponibilidad", "imagen"]
    search_fields = ["marca", "nombre"]

admin.site.register(Producto, ProductoAdmin)
