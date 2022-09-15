from asyncio.windows_events import NULL
from csv import list_dialects
from multiprocessing import context
from django.shortcuts import render
from asyncio.windows_events import NULL
from .models import Producto

# Create your views here.

def verProductos(request, id= NULL):
    if not id:
        listaProductos = Producto.objects.all()
        context = {
            'productos': listaProductos,
        }
        return render(request, 'productos/productos.html', context)
    else:
        id = int(id)
        resgProducto = Producto.objects.get(id=id)
        context = {
            'producto': resgProducto,
        }
        return render(request, 'productos/unProductos.html', context)