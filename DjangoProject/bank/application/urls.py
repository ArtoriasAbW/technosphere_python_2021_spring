"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import accounts_list, account_info, account_add
from departments.views import departments_list, department_info, department_add
from clients.views import clients_list, client_info, client_add
from transactions.views import transactions_list, transaction_info, transaction_add
from application.view import main

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('clients/', clients_list, name='clients_list'),
    path('accounts/', accounts_list, name='accounts_list'),
    path('departments/', departments_list, name='departments_list'),
    path('transactions/', transactions_list, name='transaction_list'),
    path('clients/add/', client_add, name='client_add'),
    path('accounts/add/', account_add, name='account_add'),
    path('departments/add/', department_add, name='department_add'),
    path('transactions/add/', transaction_add, name='transaction_add'),
    path('clients/<int:client_id>/', client_info, name='client_info'),
    path('accounts/<int:account_number>/', account_info, name='account_info'),
    path('departments/<int:department_id>/', department_info, name='department_info'),
    path('transactions/<int:transaction_id>/', transaction_info, name='transaction_info'),

]
