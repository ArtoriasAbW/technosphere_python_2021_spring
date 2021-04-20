from django.http import JsonResponse
from django.core import serializers
from accounts.models import Account
from transactions.models import Transaction
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def transactions_list(request):
    transactions = Transaction.objects.all()
    data = serializers.serialize('json', list(transactions))
    return JsonResponse({'transactions': data})


@require_http_methods(['GET'])
def transaction_info(request, transaction_id):
    try:
        transaction = Transaction.objects.get(pk=transaction_id)
    except Transaction.DoesNotExist:
        return JsonResponse({'status': 'транзакция не существует'})
    return JsonResponse({'Идентификатор транзакции': transaction.transaction_id,
                         'Отправитель': transaction.sender.account_number,
                         'Получатель': transaction.receiver.account_number,
                         'Время': transaction.time,
                         'Сумма': transaction.amount})


@require_http_methods(['POST'])
def transaction_add(request):
    request_params = request.POST.dict()
    transaction = Transaction(transaction_id=request_params['transaction_id'],
                              time=request_params['time'],
                              sender=Account.objects.get(pk=request_params['sender_id']),
                              receiver=Account.objects.get(pk=request_params['receiver_id']),
                              amount=request_params['amount'])
    transaction.clean_fields()  # validation
    transaction.save()
    return JsonResponse({'status': 'ok'})
