# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_todos', '0003_auto_20150908_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='incompleteCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='todos',
            name='listId',
            field=models.CharField(max_length=20),
        ),
    ]
