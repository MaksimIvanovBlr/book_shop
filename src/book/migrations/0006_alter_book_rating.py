# Generated by Django 4.1.2 on 2022-11-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("0", "0"),
                    ("6", "6"),
                    ("4", "4"),
                    ("2", "2"),
                    ("10", "10"),
                    ("8", "8"),
                    ("9", "9"),
                    ("7", "7"),
                    ("1", "1"),
                    ("5", "5"),
                    ("3", "3"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]
