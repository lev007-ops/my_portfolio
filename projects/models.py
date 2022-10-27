from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    technology = models.CharField(max_length=50, verbose_name='Технология')
    image = models.ImageField(upload_to='projects/%Y-%m-%d/',
                              verbose_name='Фото')
    github_link = models.URLField(verbose_name='Ссылка на GitHub', null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
