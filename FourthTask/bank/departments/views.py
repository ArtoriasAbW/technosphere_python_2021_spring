from django.http import JsonResponse, HttpResponseNotAllowed


# Create your views here.

def departments_list(request):
    if request.method == 'GET':
        return JsonResponse({'departments': 'list_of_departments'})
    return HttpResponseNotAllowed('Not Allowed')


def department_info(request, department_id):
    if request.method == 'GET':
        return JsonResponse({department_id: 'department_info'})
    return HttpResponseNotAllowed('Not Allowed')


def department_add(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'ok'})
    return HttpResponseNotAllowed('Not Allowed')
