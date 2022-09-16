from asyncio.windows_events import NULL
from csv import list_dialects
from multiprocessing import context
from django.shortcuts import render
from asyncio.windows_events import NULL
from .models import Carrito, Producto

# Create your views here.

def verProductos(request, id= NULL):
    if not id:
        listaProductos = Producto.objects.all()
        print('----------')
        print(listaProductos)
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

"""
Funcion para el manejo de los productos en el carrito
"""
def agregar(request, id= NULL):
    id = int(id)
    user = request.user
    regProducto = Producto.objects.get(id=id)
    existe = Carrito.objects.filter(producto = regProducto, estado = 'carrito').exists()
    if existe:
        regCarrito = Carrito.objects.get(producto = regProducto, estado = 'carrito')
        regCarrito.cantidad += 1
        regCarrito.save()
    else:
        regCarrito = Carrito(cliente = user, producto = regProducto, precio = regProducto.precio)
        regCarrito.save()

    listaProductos = Producto.objects.all()
    context = {
        'productos' : listaProductos,
    }
    return render(request, 'productos/productos.html', context)