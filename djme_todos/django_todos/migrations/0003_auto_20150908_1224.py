# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_todos', '0002_todos_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='userId',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
