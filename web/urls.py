from django.urls import path

from web.views import main_view, registration_view, project_add_view

urlpatterns = [
    path('', main_view),
    path('registration', registration_view),
    path('projects/add', project_add_view, name='projects_add')
]
