from django.http import JsonResponse, HttpResponseNotAllowed
from accounts.models import Account
from django.core import serializers
from clients.models import Client
from departments.models import Department


# Create your views here.

def accounts_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        data = serializers.serialize('json', list(accounts))
        return JsonResponse({'accounts': data})
    return HttpResponseNotAllowed('Not Allowed')


def account_info(request, account_id):
    if request.method == 'GET':
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return JsonResponse({'status': 'Аккаунт не существует'})
        return JsonResponse({'Номер счета': account.account_number,
                             'Статус': account.account_status,
                             'Баланс': account.account_balance,
                             'Дата открытия': account.opening_date,
                             'Владелец': account.client.name,
                             'Отделение': account.department.name})
    return HttpResponseNotAllowed('Not Allowed')


def account_add(request):
    if request.method == 'POST':
        request_params = request.GET.dict()  # request.POST.dict() when form-data
        account = Account(account_number=request_params['account_number'],
                          account_status=request_params['account_status'],
                          account_balance=request_params['account_balance'],
                          opening_date=request_params['opening_date'],
                          client=Client.objects.get(pk=request_params['client_id']),
                          department=Department.objects.get(pk=request_params['department_id']))
        account.clean_fields()  # validation
        account.save()
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
