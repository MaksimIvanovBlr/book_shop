# Generated by Django 4.1.2 on 2022-11-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0008_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("10", "10"),
                    ("8", "8"),
                    ("4", "4"),
                    ("0", "0"),
                    ("1", "1"),
                    ("5", "5"),
                    ("6", "6"),
                    ("2", "2"),
                    ("9", "9"),
                    ("7", "7"),
                    ("3", "3"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]
