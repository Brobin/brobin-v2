# Generated by Django 2.2 on 2020-07-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_auto_20200722_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=128),
        ),
    ]