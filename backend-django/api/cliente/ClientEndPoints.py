import json

from ..models import Cliente
from django.http import JsonResponse

def get_clientes():
    clientes = Cliente.objects.all()

    dados = [
        cliente_to_dict(cliente)
        for cliente in clientes
    ]

    return JsonResponse(dados, safe=False)

def post_clientes(request):
    body = json.loads(request.body)

    cliente = Cliente()

    for value in ('nome', 'cpf', 'telefone', 'email'):
        setattr(cliente, value, body.get(value))

    cliente.save()
    return JsonResponse({
        'mensagem': 'Cliente cadastrado com sucesso',
        'id': cliente.id
    }, status=201)


def cliente_to_dict(cliente):
    return {
        'id': cliente.id,
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'telefone': cliente.telefone,
        'email': cliente.email,
    }