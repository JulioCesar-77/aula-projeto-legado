from .cliente import ClientEndPoints
from django.http import JsonResponse

def handle_cliente(request):
    if request.method == 'GET':
        return ClientEndPoints.get_clientes()

    if request.method == 'POST':
        return ClientEndPoints.post_clientes(request)

    return JsonResponse(
            {'erro': 'Metodo nao permitido'},
            status=405
        )
