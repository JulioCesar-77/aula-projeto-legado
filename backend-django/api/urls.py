from django.urls import path

from .views import handle_cliente, handle_cliente_by_id

urlpatterns = [
    path('clientes', handle_cliente),
    path('clientes/<int:id>', handle_cliente_by_id),
]