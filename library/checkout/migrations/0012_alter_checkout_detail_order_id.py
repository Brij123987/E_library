# Generated by Django 4.2.4 on 2023-12-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_alter_checkout_detail_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout_detail',
            name='order_id',
            field=models.CharField(default=4067695, max_length=99999),
        ),
    ]
