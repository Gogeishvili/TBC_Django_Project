# Generated by Django 5.1.1 on 2024-10-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
