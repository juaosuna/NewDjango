from multiprocessing import context
from django.shortcuts import render
from appProductos.models import Producto

def home(request):
    return render(request, 'home.html')

def contactenos(request):
    return render(request, 'contactenos.html')

def productos(request):
    context= {
        'productos' : Producto.objects.all()
    }
    return render(request, 'productos/productos.html', context)

def nosotros(request):
    return render(request, 'nosotros.html')

