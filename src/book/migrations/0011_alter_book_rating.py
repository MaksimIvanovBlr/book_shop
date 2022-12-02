# Generated by Django 4.1.2 on 2022-12-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0010_alter_book_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.CharField(
                choices=[
                    ("8", "8"),
                    ("4", "4"),
                    ("3", "3"),
                    ("1", "1"),
                    ("10", "10"),
                    ("9", "9"),
                    ("6", "6"),
                    ("2", "2"),
                    ("0", "0"),
                    ("7", "7"),
                    ("5", "5"),
                ],
                default="0",
                max_length=50,
                verbose_name="Рейтинг",
            ),
        ),
    ]
