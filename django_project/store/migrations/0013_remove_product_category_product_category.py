# Generated by Django 5.1.1 on 2024-10-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='store.category'),
        ),
    ]
