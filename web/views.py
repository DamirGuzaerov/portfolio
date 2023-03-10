from django.shortcuts import render

from web.forms import RegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()

menu = ['Projects', 'Skills', 'Contacts']


def main_view(request):
    return render(request, 'web/main.html', {'menu': menu})


def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data['email'],username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
    return render(request, 'web/registration.html',
                  {'form': form, 'menu': menu})


def projects_view(request):
    form = RegistrationForm()
    return render(request, 'web/projects.html', {'form': form, 'menu': menu})
