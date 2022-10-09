from django.db import models


class Guide(models.Model):
    """layout for reference"""

    discripton = models.TextField(
        verbose_name='Описание',
        max_length=100,
        blank=True,
        null=True
    )

    # def __str__(self):
    #     return self.name


class Genre(Guide):
    """books reference book for genres"""
    name = models.CharField(
        verbose_name="Назание жанра",
        max_length=40
    )

    def __str__(self):
        return self.name


class Author(Guide):
    """reference of authors"""
    name = models.CharField(
        verbose_name='Имя автора',
        max_length=40
    )
    surname = models.CharField(
        verbose_name='Фамилия автора',
        max_length=40
    )
    birthday = models.DateField(
        verbose_name='Дата рождения'
    )
    date_of_death = models.DateField(
        verbose_name='Дата смерти',
        blank=True,
        null=True
    )
    nation = models.CharField(
        verbose_name='Страна',
        max_length=40,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Series(Guide):
    """reference book series"""
    name = models.CharField(
        verbose_name='Название серии',
        max_length=40
    )

    def __str__(self):
        return self.name


class Publishing(Guide):
    """ reference of publishing"""
    name = models.CharField(
        verbose_name='Имя издательства',
        max_length=40
    )

    def __str__(self):
        return self.name
