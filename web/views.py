from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

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
