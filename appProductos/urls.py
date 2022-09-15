from django.urls import path
from . import views

urlpatterns ={
    path('producto/', views.verProductos, name="productos"),
    path('producto/<str:id>', views.verProductos, name="producto"),
}