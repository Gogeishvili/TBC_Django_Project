# Generated by Django 5.1.1 on 2024-10-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='store.category'),
        ),
    ]