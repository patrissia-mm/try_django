# Generated by Django 4.0.6 on 2022-07-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]