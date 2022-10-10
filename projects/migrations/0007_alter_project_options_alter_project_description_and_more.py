# Generated by Django 4.1 on 2022-10-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/%Y-%m-%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=50, verbose_name='Технология'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterModelTable(
            name='project',
            table='projects',
        ),
    ]
