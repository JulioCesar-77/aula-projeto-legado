from .models import Cliente
from django.http import JsonResponse

def get_clientes(request):
    if request.method != 'GET':
        return JsonResponse(
            {'erro': 'Método não permitido'},
            status=405
        )

    clientes = Cliente.objects.all()

    dados = [
        cliente_to_dict(cliente)
        for cliente in clientes
    ]

    return JsonResponse(dados, safe=False)


def cliente_to_dict(cliente):
    return {
        'id': cliente.id,
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'telefone': cliente.telefone,
        'email': cliente.email,
    }