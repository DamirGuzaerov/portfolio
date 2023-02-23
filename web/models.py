from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

User = get_user_model()


class Skill(models.Model):
    name = models.CharField(max_length=128)
    level = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])


class Education(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    skills = models.ManyToManyField(Skill)


class Experience(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=512)


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    link_to_source_code = models.CharField(max_length=512)
    link_to_production = models.CharField(max_length=512)
    preview_img = models.ImageField(upload_to='project_previews/', null=False, blank=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

