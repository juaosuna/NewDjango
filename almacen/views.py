from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contactenos(request):
    return render(request, 'contactenos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def Productos(request):
    return render(request, 'productos/productos.html')