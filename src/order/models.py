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
    def total_price(self):
        all_books_positions = self.cart.all()
        total_price = 0
        for book_position in all_books_positions:
            total_price += book_position.price_per_position
        return total_price

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
    @property
    def price_per_position(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.book)

class Statuses(models.Model):
    status = models.CharField(
        verbose_name='статус',
        max_length=40
    )
    def __str__(self):
        return self.status


class Order(models.Model):
    cart = models.OneToOneField(
        'order.Cart',
        verbose_name='корзина',
        related_name='order',
        on_delete=models.PROTECT
    )

    status = models.ForeignKey(
        'order.Statuses',
        verbose_name='статус заказа',
        related_name='statuses',
        on_delete=models.PROTECT,

    )
    name = models.CharField(
        verbose_name='ФИО',
        max_length= 200
    )
    
    telefon_number = models.PositiveIntegerField(
        verbose_name='номер телефона'
    )
    email_adress = models.EmailField(
        verbose_name='email',
         max_length=254)
    
    adress = models.TextField(
        verbose_name='Адрес',
        max_length=200
    )

    created_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )

    additional_information = models.TextField(
        verbose_name='Дополнительная информация',
        max_length=500,
        blank=True,
        null=True
    )
    

    def __str__(self):
        return str(self.pk)