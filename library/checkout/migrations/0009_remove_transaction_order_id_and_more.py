# Generated by Django 4.2.4 on 2023-12-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_rename_status_id_transaction_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='checkout_detail',
            name='order_id',
            field=models.CharField(default=9325152, max_length=99999),
        ),
    ]
