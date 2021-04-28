from django.shortcuts import render
from django.http import HttpResponse


from users.forms import UserForm


def test_view(request):
    if request.method == 'POST':

        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')

    else:
        form = UserForm()

    return render(request, 'test_form.html', {'utl': 'regform', 'form': form})
