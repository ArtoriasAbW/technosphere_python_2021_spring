from django.shortcuts import render
from django.http import HttpResponseNotAllowed


def main(request):
    if request.method == 'GET':
        request_params = request.GET.dict()
        return render(request,
                      'index.html',
                      context={'data': request_params})
    return HttpResponseNotAllowed('Not Allowed')

