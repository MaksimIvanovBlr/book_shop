# Generated by Django 4.1.2 on 2022-11-23 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_order_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="order",
                to="order.cart",
                verbose_name="корзина",
            ),
        ),
    ]
