# Generated by Django 4.0.4 on 2022-05-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_exist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='customer',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
