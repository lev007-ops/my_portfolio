from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст поста')
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано в')
    last_modified = models.DateTimeField(auto_now=True,
                                         verbose_name='Последние изменение')
    categories = models.ManyToManyField('Category', related_name='posts',
                                        verbose_name='Категории')

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.CharField(max_length=60, verbose_name='Автор')
    body = models.TextField(verbose_name='Текст комментария')
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано в')
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             verbose_name='Пост')

    def __str__(self) -> str:
        return self.body

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
