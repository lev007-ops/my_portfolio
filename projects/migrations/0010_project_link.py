# Generated by Django 4.1 on 2022-10-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_github_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(null=True, verbose_name='Ссылка на проект'),
        ),
    ]