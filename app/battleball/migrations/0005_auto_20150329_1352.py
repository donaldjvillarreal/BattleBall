# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0004_auto_20150328_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dateJoined',
            field=models.DateTimeField(verbose_name='Date Joined'),
            preserve_default=True,
        ),
    ]
