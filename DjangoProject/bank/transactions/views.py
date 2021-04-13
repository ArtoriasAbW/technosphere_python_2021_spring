from django.http import JsonResponse, HttpResponseNotAllowed
from django.core import serializers
from accounts.models import Account
from transactions.models import Transaction


# Create your views here.

def transactions_list(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        data = serializers.serialize('json', list(transactions))
        return JsonResponse({'transactions': data})
    return HttpResponseNotAllowed('Not Allowed')


def transaction_info(request, transaction_id):
    if request.method == 'GET':
        try:
            transaction = Transaction.objects.get(pk=transaction_id)
        except Transaction.DoesNotExist:
            return JsonResponse({'status': 'транзакция не существует'})
        return JsonResponse({'Идентификатор транзакции': transaction.transaction_id,
                             'Отправитель': transaction.sender.account_number,
                             'Получатель': transaction.receiver.account_number,
                             'Время': transaction.time,
                             'Сумма': transaction.amount})
    return HttpResponseNotAllowed('Not Allowed')


def transaction_add(request):
    if request.method == 'POST':
        request_params = request.GET.dict()  # request.POST.dict() when form-data
        transaction = Transaction(transaction_id=request_params['transaction_id'],
                                  time=request_params['time'],
                                  sender=Account.objects.get(pk=request_params['sender_id']),
                                  receiver=Account.objects.get(pk=request_params['receiver_id']),
                                  amount=request_params['amount'])
        transaction.clean_fields()  # validation
        transaction.save()
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
