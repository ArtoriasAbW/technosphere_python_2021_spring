from django.http import JsonResponse
from django.core import serializers
from departments.models import Department
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def departments_list(request):
    departments = list(Department.objects.all())
    data = serializers.serialize('json', departments)
    return JsonResponse({'departments': data})


@require_http_methods(['GET'])
def department_info(request, department_id):
    try:
        department = Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        return JsonResponse({'status': 'Департамент не существует'})
    return JsonResponse({'Название': department.name,
                         'Адрес': department.address,
                         'Номер телефона': department.phone_number})


@require_http_methods(['POST'])
def department_add(request):
    request_params = request.GET.dict()  # request.POST.dict() when form-data
    name = request_params['name']
    address = request_params['address']
    phone_number = request_params['phone_number']
    department = Department(name=name, address=address, phone_number=phone_number)
    department.save()
    return JsonResponse({'status': 'ok'})
