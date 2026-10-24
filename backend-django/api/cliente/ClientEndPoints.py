import json

from django.shortcuts import get_object_or_404

from ..models import Cliente
from django.http import JsonResponse, HttpResponse

# aq é a logica
def get_clientes():
    clientes = Cliente.objects.all()

    dados = [
        cliente_to_dict(cliente)
        for cliente in clientes
    ]

    return JsonResponse(dados, safe=False, status=200)

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

def get_cliente_by_id(id):
    cliente = get_object_or_404(Cliente, id=id)

    return JsonResponse(cliente_to_dict(cliente), safe=False, status=200)

def put_cliente_by_id(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    body = json.loads(request.body)

    for value in ('nome', 'cpf', 'telefone', 'email'):
        setattr(cliente, value, body.get(value))

    cliente.save()
    return JsonResponse(cliente_to_dict(cliente), status=200)

def delete_cliente_by_id(id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()

    return HttpResponse(status=204)

def cliente_to_dict(cliente):
    return {
        'id': cliente.id,
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'telefone': cliente.telefone,
        'email': cliente.email,
    }