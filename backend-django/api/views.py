from .cliente import ClientEndPoints
from django.http import JsonResponse, HttpResponseBadRequest


def handle_cliente(request):
    if request.method == 'GET':
        return ClientEndPoints.get_clientes()

    if request.method == 'POST':
        return ClientEndPoints.post_clientes(request)

    return JsonResponse(
            {'erro': 'Metodo nao permitido'},
            status=405
        )

def handle_cliente_by_id(request, id=None):
    if id is None:
        return HttpResponseBadRequest()

    if request.method == 'GET':
        return ClientEndPoints.get_cliente_by_id(id)
    if request.method == 'PUT':
        return ClientEndPoints.put_cliente_by_id(request, id)
    if request.method == 'DELETE':
        return ClientEndPoints.delete_cliente_by_id(id)

    return JsonResponse(
            {'erro': 'Metodo nao permitido'},
            status=405
        )
