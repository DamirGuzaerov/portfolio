# Generated by Django 4.1.7 on 2023-02-23 21:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('level', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('link_to_source_code', models.CharField(max_length=512)),
                ('link_to_production', models.CharField(max_length=512)),
                ('preview_img_url', models.CharField(max_length=512)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.experience')),
                ('skills', models.ManyToManyField(to='web.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('skills', models.ManyToManyField(to='web.skill')),
            ],
        ),
    ]
