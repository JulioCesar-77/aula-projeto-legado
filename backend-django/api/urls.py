from django.urls import path

from .views import handle_cliente

urlpatterns = [
    path('clientes', handle_cliente),
]