from django.http import JsonResponse, HttpResponseNotAllowed


# Create your views here.

def accounts_list(request):
    if request.method == 'GET':
        return JsonResponse({'accounts': 'list_of_accounts'})
    return HttpResponseNotAllowed('Not Allowed')


def account_info(request, account_id):
    if request.method == 'GET':
        return JsonResponse({account_id: 'account_info'})
    return HttpResponseNotAllowed('Not Allowed')


def account_add(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
