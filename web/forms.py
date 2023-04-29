from django import forms
from django.contrib.auth import get_user_model

from web.models import Project, Skill

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            self.add_error('password_confirm', 'Passwords are not the same')
        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class ProjectAddForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Project
        fields = ('name', 'description', 'link_to_source_code', 'preview_img', 'skills')


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'level')


class ProjectFiltersForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Поиск"}), required=False)
