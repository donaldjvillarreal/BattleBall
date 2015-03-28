# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0003_board_boardstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boardState', models.CharField(default=0, max_length=30)),
                ('homeTeam', models.CharField(max_length=30)),
                ('awayTeam', models.CharField(max_length=30)),
                ('homeScore', models.IntegerField(default=0)),
                ('awayScore', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
