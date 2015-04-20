# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battleball', '0005_auto_20150329_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=250, verbose_name=b'URL', blank=True)),
                ('Creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='game',
            old_name='boardState',
            new_name='boardFile',
        ),
        migrations.AddField(
            model_name='game',
            name='turn',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
