# Generated by Django 4.1.2 on 2022-12-08 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0014_alter_book_rating"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentToBook",
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
                (
                    "message",
                    models.TextField(
                        max_length=1000, verbose_name="Комментарий к книге"
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="author_comment_book",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="автор комментария",
                    ),
                ),
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="book_comment",
                        to="book.book",
                        verbose_name="Комментируемая книга",
                    ),
                ),
            ],
        ),
    ]
