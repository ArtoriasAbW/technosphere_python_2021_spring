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
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from application.views import home, login, main

from clients.views import ClientViewSet
from departments.views import DepartmentViewSet
from accounts.views import AccountViewSet
from transactions.views import TransactionViewSet
from users.views import CustomUserViewSet


router = DefaultRouter()
router.register(r'clients', ClientViewSet, 'clients')
router.register(r'departments', DepartmentViewSet, 'departments')
router.register(r'accounts', AccountViewSet, 'accounts')
router.register(r'transactions', TransactionViewSet, 'transactions')
router.register(r'users', CustomUserViewSet, 'users')


urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += router.urls
