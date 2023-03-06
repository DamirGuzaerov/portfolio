from django.shortcuts import render

from web.forms import RegistrationForm

menu = ['Projects', 'Skills', 'Contacts']


def main_view(request):
    return render(request, 'web/main.html', {'menu': menu})


def registration_view(request):
    form = RegistrationForm()
    return render(request, 'web/registration.html', {'form': form, 'menu': menu})


def projects_view(request):
    form = RegistrationForm()
    return render(request, 'web/projects.html', {'form': form, 'menu': menu})

