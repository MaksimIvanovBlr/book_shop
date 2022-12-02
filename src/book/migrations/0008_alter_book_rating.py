# Generated by Django 4.1.2 on 2022-11-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0007_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("0", "0"),
                    ("1", "1"),
                    ("4", "4"),
                    ("6", "6"),
                    ("3", "3"),
                    ("5", "5"),
                    ("9", "9"),
                    ("10", "10"),
                    ("8", "8"),
                    ("7", "7"),
                    ("2", "2"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]