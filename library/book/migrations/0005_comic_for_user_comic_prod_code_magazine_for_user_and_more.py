# Generated by Django 4.2.4 on 2023-09-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_comic_comic_image_magazine_magazine_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='comic',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='magazine',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='magazine',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='newspaper',
            name='for_user',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AddField(
            model_name='newspaper',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
    ]
