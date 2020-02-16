# Generated by Django 2.1.5 on 2020-02-15 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]