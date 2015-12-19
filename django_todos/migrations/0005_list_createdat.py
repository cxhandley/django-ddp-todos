# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('django_todos', '0004_auto_20150909_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 11, 27, 52, 487531, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
