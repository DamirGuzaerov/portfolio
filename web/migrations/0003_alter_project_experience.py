# Generated by Django 4.1.7 on 2023-03-21 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_project_preview_img_url_project_preview_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='experience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.experience'),
        ),
    ]
