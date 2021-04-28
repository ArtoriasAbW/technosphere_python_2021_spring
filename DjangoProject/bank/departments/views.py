from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from departments.serializers import DepartmentSerializer
from departments.models import Department
from departments.forms import DepartmentForm


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


def department_add(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return JsonResponse({'status': 'department added', 'department_id': department.id})
    else:
        form = DepartmentForm()

    return render(request, 'test_form.html', {'url': 'department_form', 'form': form})
