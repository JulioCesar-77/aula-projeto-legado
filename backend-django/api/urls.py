from django.urls import path

from .views import handle_vaga, handle_vaga_by_id

from .views import handle_cliente, handle_cliente_by_id
from .views import handle_veiculo, handle_veiculo_by_id

urlpatterns = [
    path('clientes', handle_cliente),
    path('clientes/<int:id>', handle_cliente_by_id),

    path('veiculos', handle_veiculo),
    path('veiculos/<int:id>', handle_veiculo_by_id),

    path('vagas', handle_vaga),
    path('vagas/', handle_vaga),

    path('vagas/<int:id>', handle_vaga_by_id),
    path('vagas/<int:id>/', handle_vaga_by_id),
]


# aq tem os endpoints