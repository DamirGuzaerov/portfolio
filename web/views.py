from django.shortcuts import render, redirect, get_object_or_404

from web.forms import RegistrationForm, AuthForm, ProjectAddForm, SkillForm, ProjectFiltersForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from web.models import Project, Skill
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator

User = get_user_model()


def main_view(request):
    projects = Project.objects.all()

    filter_form = ProjectFiltersForm(request.GET)
    filter_form.is_valid()
    filters = filter_form.cleaned_data

    if filters['search']:
        projects = projects.filter(name__icontains=filters['search'])

    total_count = projects.count()

    page = request.GET.get('page', 1)
    pagination = Paginator(projects, per_page=10)

    return render(request, 'web/main.html', {'projects': pagination.get_page(page),
                                             'filter_form': filter_form,
                                             "total_count": total_count}, )


def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data['email'], username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main')
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


@user_passes_test(lambda u: u.is_superuser, 'main')
@login_required
def project_add_view(request, id=None):
    project = None
    if id is not None:
        project = get_object_or_404(Project, id=id)
    form = ProjectAddForm(instance=project)
    if request.method == 'POST':
        form = ProjectAddForm(data=request.POST, files=request.FILES, instance=project)
        if form.is_valid():
            form.save()
            redirect('main')

    return render(request, 'web/project_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser, 'main')
@login_required
def projects_delete_view(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('main')


@user_passes_test(lambda u: u.is_superuser, 'main')
@login_required
def skill_view(request):
    skills = Skill.objects.all()
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    return render(request, 'web/skills.html', {'skills': skills, 'form': form})


@user_passes_test(lambda u: u.is_superuser, 'main')
@login_required
def skills_delete_view(request, id):
    skill = get_object_or_404(Skill, id=id)
    skill.delete()
    return redirect('skills')
