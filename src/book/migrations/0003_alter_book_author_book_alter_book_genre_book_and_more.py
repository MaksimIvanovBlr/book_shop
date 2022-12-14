# Generated by Django 4.1.2 on 2022-11-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("guide", "0002_alter_genre_description_alter_series_description"),
        ("book", "0002_alter_book_author_book_alter_book_genre_book_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author_book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="authorbook",
                to="guide.author",
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre_book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="genrebook",
                to="guide.genre",
                verbose_name="Жанр",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="publishing_book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="publishingbook",
                to="guide.publishing",
                verbose_name="Издательство",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("0", "0"),
                    ("4", "4"),
                    ("2", "2"),
                    ("6", "6"),
                    ("8", "8"),
                    ("7", "7"),
                    ("9", "9"),
                    ("1", "1"),
                    ("5", "5"),
                    ("3", "3"),
                    ("10", "10"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="series_book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="seriesbook",
                to="guide.series",
                verbose_name="Серия",
            ),
        ),
    ]
