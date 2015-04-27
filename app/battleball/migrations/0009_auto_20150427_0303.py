# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0008_auto_20150427_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
