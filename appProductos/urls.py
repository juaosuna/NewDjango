from django.urls import path
from . import views

urlpatterns =[
    path('producto/', views.verProductos, name="producto"),
    path('producto/<str:id>', views.verProductos, name="producto"),
    path('carrito/<str:id>', views.agregar, name="carrito"),
]