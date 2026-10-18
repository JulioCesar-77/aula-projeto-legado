from django.urls import path

from .views import get_clientes

urlpatterns = [
    path('clientes', get_clientes),
]