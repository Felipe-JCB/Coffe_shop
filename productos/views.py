from django.urls import reverse_lazy
from django.views import generic
from .formularios import ProductoForm
from .models import Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductoSerializer

# Create your views here.
class ProductoFormView(generic.FormView):
    template_name = "productos/formulario.html"
    form_class = ProductoForm
    success_url = reverse_lazy('agregar_producto')

    def form_valid(self, form):
        # Aquí puedes realizar acciones adicionales con el formulario válido
        form.guardar()
        return super().form_valid(form)
    
class ProductoListView(generic.ListView):
    model = Producto
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"


class ProductoListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Producto.objects.all()
        serializer = ProductoSerializer(products, many=True)
        return Response(serializer.data)