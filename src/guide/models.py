from django.db import models
from django.urls import reverse_lazy


class Genre(models.Model):
    """справочник жанров"""
    name = models.CharField(
        verbose_name="Назание жанра",
        max_length=40
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail-genre', kwargs ={'pk':self.pk})


class Author(models.Model):
    """справочник авторов"""
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=40
    )
    surname = models.CharField(
        verbose_name='Фамилия автора',
        max_length=40,
        blank=True,
        null=True

    )
    birthday = models.DateField(
        verbose_name='Дата рождения'
    )

    nation = models.CharField(
        verbose_name='Страна',
        max_length=40,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('detail-author', kwargs ={'pk':self.pk})
    

class Series(models.Model):
    """серия книг"""
    name = models.CharField(
        verbose_name='Название серии',
        max_length=40
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail-series', kwargs ={'pk':self.pk}) 


class Publishing(models.Model):
    """ издательство"""
    name = models.CharField(
        verbose_name='Название издательства',
        max_length=40
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail-publishing', kwargs ={'pk':self.pk})
