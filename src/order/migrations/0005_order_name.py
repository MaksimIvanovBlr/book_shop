# Generated by Django 4.1.2 on 2022-11-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0004_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="name",
            field=models.CharField(default="name", max_length=200, verbose_name="ФИО"),
            preserve_default=False,
        ),
    ]