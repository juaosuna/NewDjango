from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contactenos(request):
    return render(request, 'contactenos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def Servicios(request):
    return render(request, 'servicios.html')