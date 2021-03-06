# Generated by Django 2.1.5 on 2020-02-15 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('products', models.ManyToManyField(to='api.Product')),
            ],
        ),
    ]
