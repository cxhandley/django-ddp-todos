# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import dddp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_todos', '0005_list_createdat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['createdAt']},
        ),
        migrations.AddField(
            model_name='list',
            name='aid',
            field=dddp.models.AleaIdField(unique=True, max_length=17, verbose_name=b'List Alea ID'),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='todos',
            name='aid',
            field=dddp.models.AleaIdField(unique=True, max_length=17, verbose_name=b'Todos Alea ID'),
        ),
    ]
