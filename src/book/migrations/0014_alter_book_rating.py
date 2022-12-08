# Generated by Django 4.1.2 on 2022-12-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0013_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("5", "5"),
                    ("6", "6"),
                    ("9", "9"),
                    ("10", "10"),
                    ("3", "3"),
                    ("2", "2"),
                    ("4", "4"),
                    ("8", "8"),
                    ("0", "0"),
                    ("7", "7"),
                    ("1", "1"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]
