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
from django.urls import path
from rest_framework.routers import DefaultRouter

from application.view import main

from clients.views import ClientViewSet
from departments.views import DepartmentViewSet, department_add
from accounts.views import AccountViewSet
from transactions.views import TransactionViewSet
from users.views import test_view

router = DefaultRouter()
router.register(r'clients', ClientViewSet, 'clients')
router.register(r'departments', DepartmentViewSet, 'departments')
router.register(r'accounts', AccountViewSet, 'accounts')
router.register(r'transactions', TransactionViewSet, 'transactions')


urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('regform/', test_view, name='test_view'),
    path('department_form/', department_add, name='department_add'),
]

urlpatterns += router.urls
