from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, ProjectAddForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from web.models import Project

User = get_user_model()


def main_view(request):
    projects = Project.objects.all()
    return render(request, 'web/main.html', {'projects': projects})


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


def authorization_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(**form.cleaned_data)
            print(user)
            if user is None:
                form.add_error(None, 'Email or password is not correct')
            else:
                login(request, user)
                return redirect("main")

    return render(request, 'web/auth.html',
                  {'form': form})


def logout_view(request):
    logout(request)
    return redirect("main")


def project_add_view(request, id=None):
    project = None
    if id is not None:
        project = Project.objects.get(id=id)
    form = ProjectAddForm(instance=project)
    if request.method == 'POST':
        form = ProjectAddForm(data=request.POST, files=request.FILES, instance=project)
        if form.is_valid():
            form.save()
            redirect('main')

    return render(request, 'web/project_form.html', {'form': form})
