# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0002_board_team_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='boardState',
            field=models.CharField(default=0, max_length=30),
            preserve_default=True,
        ),
    ]
