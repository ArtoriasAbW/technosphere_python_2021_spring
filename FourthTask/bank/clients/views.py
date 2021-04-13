from django.http import JsonResponse, HttpResponseNotAllowed


# Create your views here.

def clients_list(request):
    if request.method == 'GET':
        return JsonResponse({'clients': 'list_of_clients'})
    return HttpResponseNotAllowed('Not Allowed')


def client_info(request, client_id):
    if request.method == 'GET':
        return JsonResponse({client_id: 'client_info'})
    return HttpResponseNotAllowed('Not Allowed')


def client_add(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
