# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('incompleteCount', models.IntegerField()),
                ('userId', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('listId', models.ForeignKey(to='django_todos.List')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
