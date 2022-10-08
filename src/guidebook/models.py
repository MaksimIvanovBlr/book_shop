from django.db import models


class GenreBook(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=40
    )
    discription = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name


class AuthorBook(models.Model):
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=40
    )
    discription = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

