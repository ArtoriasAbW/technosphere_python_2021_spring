from django.http import JsonResponse, HttpResponseNotAllowed
from django.core import serializers
from departments.models import Department


# Create your views here.

def departments_list(request):
    if request.method == 'GET':
        departments = list(Department.objects.all())
        data = serializers.serialize('json', departments)
        return JsonResponse({'departments': data})
    return HttpResponseNotAllowed('Not Allowed')


def department_info(request, department_id):
    if request.method == 'GET':
        department = Department.objects.get(pk=department_id)
        return JsonResponse({'Название': department.name,
                             'Адрес': department.address,
                             'Номер телефона': department.phone_number})
    return HttpResponseNotAllowed('Not Allowed')


def department_add(request):
    if request.method == 'POST':
        request_params = request.GET.dict()  # request.POST.dict() when form-data
        name = request_params['name']
        address = request_params['address']
        phone_number = request_params['phone_number']
        department = Department(name=name, address=address, phone_number=phone_number)
        department.save()
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
