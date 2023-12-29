from django.http import Http404, HttpResponse, HttpResponseRedirect #, JsonResponse
from django.shortcuts import render, get_object_or_404

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.

#/productos
def index(request): 
    #return HttpResponse("Hola mundo!!!")
    #productos = Producto.objects.all().values()
    #productos = Producto.objects.filter(puntaje=3)
    #productos = Producto.objects.get(id=1)
    #print(productos)
    #return HttpResponse(productos[0].nombre)
    #return JsonResponse(list(productos), safe=False)
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
    
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    return render(request,'detalle.html', context={'producto': producto})

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )