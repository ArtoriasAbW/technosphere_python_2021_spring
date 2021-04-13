from django.http import JsonResponse, HttpResponseNotAllowed
from clients.models import Client
from django.core import serializers


# Create your views here.

def clients_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        data = serializers.serialize('json', list(clients))
        return JsonResponse({'clients': data})
    return HttpResponseNotAllowed('Not Allowed')


def client_info(request, client_id):
    if request.method == 'GET':
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return JsonResponse({'status': 'Клиент не существует'})
        return JsonResponse({'Имя': client.name,
                             'Номер телефона': client.phone_number,
                             'email': client.email,
                             'Адрес': client.address,
                             'Дата регистрации': client.registration_date})
    return HttpResponseNotAllowed('Not Allowed')


def client_add(request):
    if request.method == 'POST':
        request_params = request.GET.dict()  # request.POST.dict() when form-data
        client = Client(name=request_params['name'],
                        phone_number=request_params['phone_number'],
                        email=request_params['email'],
                        address=request_params['address'],
                        registration_date=request_params['registration_date'])
        client.save()
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
