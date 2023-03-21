from django.shortcuts import render

from web.forms import RegistrationForm, ProjectAddForm
from django.contrib.auth import get_user_model

User = get_user_model()


def base_view(request):
    return render(request, 'web/base.html')


def main_view(request):
    return render(request, 'web/main.html')


def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data['email'], username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
    return render(request, 'web/registration.html',
                  {'form': form})


def projects_view(request):
    form = RegistrationForm()
    return render(request, 'web/projects.html', {'form': form})


def project_add_view(request):
    form = ProjectAddForm()
    return render(request, 'web/project_form.html', {'form': form})
