from django.db import models

class ExchangeRate(models.Model):
    rate = models.DecimalField(
        verbose_name='Курс',
        max_digits=5,
        decimal_places=2
    )

    last_change = models.DateField(
        verbose_name='Дата последнего изменение карточки',
        auto_now=True
    )
