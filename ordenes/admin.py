from django.contrib import admin
from .models import Orden, OrdenProducto
# Register your models here.
class OrdenProductoInLineAdmin(admin.TabularInline):
    model = OrdenProducto
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    model = Orden
    inlines = [OrdenProductoInLineAdmin]

admin.site.register(Orden, OrdenAdmin)
