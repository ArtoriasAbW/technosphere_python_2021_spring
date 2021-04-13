from django.http import JsonResponse, HttpResponseNotAllowed


# Create your views here.

def transactions_list(request):
    if request.method == 'GET':
        return JsonResponse({'transactions': 'list_of_transactions'})
    return HttpResponseNotAllowed('Not Allowed')


def transaction_info(request, transaction_id):
    if request.method == 'GET':
        return JsonResponse({transaction_id: 'transaction_info'})
    return HttpResponseNotAllowed('Not Allowed')


def transaction_add(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
