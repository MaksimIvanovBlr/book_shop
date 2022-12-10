# Generated by Django 4.1.2 on 2022-12-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0015_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("3", "3"),
                    ("5", "5"),
                    ("2", "2"),
                    ("4", "4"),
                    ("8", "8"),
                    ("1", "1"),
                    ("6", "6"),
                    ("0", "0"),
                    ("10", "10"),
                    ("7", "7"),
                    ("9", "9"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]