from django.http import JsonResponse
from clients.models import Client
from django.core import serializers
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def clients_list(request):
    clients = Client.objects.all()
    data = serializers.serialize('json', list(clients))
    return JsonResponse({'clients': data})


@require_http_methods(['GET'])
def client_info(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return JsonResponse({'status': 'Клиент не существует'})
    return JsonResponse({'Имя': client.name,
                         'Номер телефона': client.phone_number,
                         'email': client.email,
                         'Адрес': client.address,
                         'Дата регистрации': client.registration_date})


@require_http_methods(['POST'])
def client_add(request):
    request_params = request.POST.dict()  # request.POST.dict() when form-data
    client = Client(name=request_params['name'],
                    phone_number=request_params['phone_number'],
                    email=request_params['email'],
                    address=request_params['address'],
                    registration_date=request_params['registration_date'])
    client.save()
    return JsonResponse({'status': 'ok'})
