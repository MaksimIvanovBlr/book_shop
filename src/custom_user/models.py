from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

inbuilt_user = get_user_model()


class ExtendUser(models.Model):
    extend_user = models.OneToOneField(
        inbuilt_user,
        verbose_name='user',
        related_name='extenduser',
        on_delete=models.PROTECT
    )

    phone = models.CharField(
        max_length=17,
        verbose_name='Номер телефона',
    )
    country = models.CharField(
        max_length=25,
        verbose_name='Страна',
    )
    city = models.CharField(
        max_length=25,
        verbose_name='Город'
    )
    index = models.PositiveIntegerField(
        verbose_name='Индекс'
    )
    adress1 = models.CharField(
        max_length=50,
        verbose_name='Адрес'
    )
    adress2 = models.CharField(
        max_length=50,
        verbose_name='Дополнительный адрес',
        default='Не указан',
        blank=True,
        null=True
    )
    information = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.extend_user)

# Create your models here.
