import json

from ..models import Veiculo
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from ..models import Veiculo, Cliente

def get_veiculos(request):
    veiculos = Veiculo.objects.all()

    dados = [
        veiculo_to_dict(veiculo)
        for veiculo in veiculos
    ]

    return JsonResponse(dados, safe=False, status=200)

def post_veiculos(request):
    body = json.loads(request.body)

    veiculo = Veiculo()
    for value in('placa', 'marca', 'modelo', 'cor'):
        setattr(veiculo, value, body.get(value))

    cliente_id = body.get('clienteId')
    veiculo.cliente = get_object_or_404(Cliente, id=cliente_id)

    veiculo.save()
    return JsonResponse({
            'mensagem': 'Veículo cadastrado com sucesso',
            'id': veiculo.id
    }, status=201)

def get_veiculo_by_id(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)

    return JsonResponse(veiculo_to_dict(veiculo), status=200)

def delete_veiculo_by_id(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    return HttpResponse(status=204)

def put_veiculo_by_id(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    body = json.loads(request.body)

    for value in ('placa', 'marca', 'modelo', 'cor'):
        setattr(veiculo, value, body.get(value))

    veiculo.save()
    return JsonResponse(veiculo_to_dict(veiculo), status=200)

def veiculo_to_dict(veiculo):
    return {
        'id': veiculo.id,
        'placa': veiculo.placa,
        'marca': veiculo.marca,
        'modelo': veiculo.modelo,
        'cor': veiculo.cor,
        'clienteId': veiculo.cliente_id,
        'clienteNome': veiculo.cliente.nome,
    }
