from django.urls import path

from web.views import main_view, registration_view, authorization_view, logout_view, project_add_view, skill_view, \
    skills_delete_view

urlpatterns = [
    path('', main_view, name="main"),
    path('registration', registration_view, name="registration"),
    path('auth', authorization_view, name="auth"),
    path('logout', logout_view, name="logout"),
    path('projects/add', project_add_view, name='projects_add'),
    path('projects/<int:id>/', project_add_view, name='projects_edit'),
    path('skills', skill_view, name='skills'),
    path('skills/<int:id>/delete', skills_delete_view, name='skills_delete'),
]
