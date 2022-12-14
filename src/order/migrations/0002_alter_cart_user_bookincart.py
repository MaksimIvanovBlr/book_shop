# Generated by Django 4.1.2 on 2022-11-21 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_alter_book_rating"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user_cart",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Корзина пользователя",
            ),
        ),
        migrations.CreateModel(
            name="BookInCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1, verbose_name="количество")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="цена"
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(auto_now=True, verbose_name="дата изменения"),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="book_in_cart",
                        to="book.book",
                        verbose_name="книга в корзине",
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="cart",
                        to="order.cart",
                        verbose_name="корзина",
                    ),
                ),
            ],
        ),
    ]
