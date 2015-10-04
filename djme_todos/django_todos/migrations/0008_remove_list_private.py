# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_todos', '0007_auto_20151004_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='private',
        ),
    ]
