# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150328_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='script',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='style',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
