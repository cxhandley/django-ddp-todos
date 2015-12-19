# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dddp.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_todos', '0006_auto_20151004_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='aid',
            field=dddp.models.AleaIdField(unique=True, max_length=17, verbose_name=b'Alea ID'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='aid',
            field=dddp.models.AleaIdField(unique=True, max_length=17, verbose_name=b'Alea ID'),
        ),
    ]
