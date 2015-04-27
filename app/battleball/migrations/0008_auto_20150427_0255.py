# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0007_auto_20150421_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameroom',
            name='Creator',
        ),
        migrations.DeleteModel(
            name='GameRoom',
        ),
    ]
