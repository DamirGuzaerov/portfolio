# Generated by Django 4.1.7 on 2023-04-29 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_project_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rate',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
