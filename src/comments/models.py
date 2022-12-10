from django.db import models
from django.contrib.auth import get_user_model
from book import models as b_models

User = get_user_model()


class CommentToBook(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='автор комментария',
        related_name='author_comment_book',

    )
    book = models.ForeignKey(
        'book.Book',
        on_delete=models.PROTECT,
        verbose_name='Комментируемая книга',
        related_name='book_comment',

    )

    message = models.TextField(
        verbose_name='Комментарий к книге',
        max_length=1000
    )

    create_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True

    )
    # def __str__(self):
    #     return str(self.pk)


class CommentToOrder(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Автор комментария',
        related_name='author_comment_order',

    )
    order = models.ForeignKey(
        'order.Order',
        on_delete=models.PROTECT,
        verbose_name='Комментируемый заказ',
        related_name='order_comment',

    )

    message = models.TextField(
        verbose_name='комментарий к заказу',
        max_length=1000
    )

    create_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True

    )

    # def __str__(self):
    #     return str(self.pk)
