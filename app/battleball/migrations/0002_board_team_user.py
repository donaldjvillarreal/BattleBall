# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battleball', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('homeTeam', models.CharField(max_length=30)),
                ('awayTeam', models.CharField(max_length=30)),
                ('homeScore', models.IntegerField(default=0)),
                ('awayScore', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamName', models.CharField(max_length=30)),
                ('gamesPlayed', models.IntegerField(default=0)),
                ('gamesWon', models.IntegerField(default=0)),
                ('rank', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullName', models.CharField(max_length=30)),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dateJoined', models.DateTimeField(verbose_name=b'Date Joined')),
                ('team', models.ForeignKey(to='battleball.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
