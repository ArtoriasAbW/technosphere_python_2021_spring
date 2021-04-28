from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from departments.serializers import DepartmentSerializer
from departments.models import Department
from departments.forms import DepartmentForm


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


def department_form(request):
    if request.method == 'POST':

        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = Department(name=form.cleaned_data['name'],
                                    address=form.cleaned_data['address'],
                                    phone_number=form.cleaned_data['phone_number'])
            department.save()
            return HttpResponse('department added')

    else:
        form = DepartmentForm()

    return render(request, 'test_form.html', {'url': 'department_form', 'form': form})
