# Generated by Django 4.1 on 2022-09-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/%Y-%m-%d/'),
        ),
    ]
