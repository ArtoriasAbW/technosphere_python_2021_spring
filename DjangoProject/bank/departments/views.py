from rest_framework import viewsets
from rest_framework.response import Response

from departments.serializers import DepartmentSerializer
from departments.models import Department
from users.models import CustomUser
from django.core.mail import send_mail


def log_on_email(func):
    def wrapper(self, serializer, *args, **kwargs):
        response = func(self, serializer, *args, **kwargs)
        send_mail('Новый объект', 'Добавлено новое отделение в базу данных', 'seleznev.pavlex@gmail.com', ['seleznev.pavlex@gmail.com'])
        return response
    return wrapper


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        auth_user = self.request.user
        if not auth_user.is_superuser:
            return Department.objects.filter(user=CustomUser.objects.get(username=auth_user))
        else:
            return Department.objects.all()

    @log_on_email
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
