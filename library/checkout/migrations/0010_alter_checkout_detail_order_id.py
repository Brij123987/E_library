# Generated by Django 4.2.4 on 2023-12-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_transaction_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout_detail',
            name='order_id',
            field=models.CharField(default=238654, max_length=99999),
        ),
    ]
