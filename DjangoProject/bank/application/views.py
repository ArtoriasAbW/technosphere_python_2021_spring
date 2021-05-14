from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from application.settings import LOGIN_URL


def need_login(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('%s?next=%s' % (LOGIN_URL, request.path))
    return wrapper


@need_login
def main(request):
    if request.method == 'GET':
        print(request.user)
        return render(request, 'index.html')
    return HttpResponseNotAllowed('Not Allowed')


def login(request):
    return render(request, 'login.html')
