# Generated by Django 5.1.1 on 2024-10-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercard',
            name='name',
            field=models.CharField(default='user card', max_length=30),
        ),
    ]