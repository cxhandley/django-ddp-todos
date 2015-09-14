from __future__ import absolute_import

from django.apps import AppConfig

def on_create_user(sender, **kwargs):
    from django.contrib.auth.models import User
    params = kwargs['params']
    return User.objects.create_user(
        username='meter_created',
        email=params['email'],
        password=params['password'],
    )

class DjmeCommonConfig(AppConfig):

    api = None
    name = 'django_todos'
    verbose_name = 'Django Metoer Todos'

    def ready(self):
        from dddp.accounts.ddp import create_user
        create_user.connect(on_create_user)
