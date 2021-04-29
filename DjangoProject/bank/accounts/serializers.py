from accounts.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_number', 'account_status', 'client', 'account_balance', 'department', 'opening_date')
