# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0006_auto_20150420_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='title',
            field=models.CharField(default=b'untitled', max_length=100, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='url',
            field=models.URLField(max_length=250, verbose_name=b'URL', blank=True),
            preserve_default=True,
        ),
    ]
