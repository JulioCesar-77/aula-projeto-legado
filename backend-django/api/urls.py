from django.urls import path

from .views import getClientes

urlpatterns = [
    path('clientes', getClientes),
]