# Generated by Django 5.1.1 on 2024-11-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_product_name_en_product_name_ka_product_slug_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug_ka',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
