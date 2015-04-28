# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0011_auto_20150428_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='str_position',
            field=models.CharField(default=b'{"xpos":-1, "ypos":-1}', max_length=20),
            preserve_default=True,
        ),
    ]
