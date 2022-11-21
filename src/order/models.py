from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Корзина пользователя',
        related_name='user_cart',
        null=True,
        blank=True
    )

class BookInCart(models.Model):
    book = models.ForeignKey(
        'book.Book',
        verbose_name='книга в корзине',
        related_name='book_in_cart',
        on_delete=models.PROTECT
    )
    cart = models.ForeignKey(
        'order.Cart',
        verbose_name='корзина',
        related_name='cart',
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        verbose_name='количество',
        default=1
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=5,
        decimal_places=2
    )
    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )

