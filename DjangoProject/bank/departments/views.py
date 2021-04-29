from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from departments.serializers import DepartmentSerializer
from departments.models import Department
from departments.forms import DepartmentForm


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
