from django.contrib import admin

from .models import Todos, List

admin.site.register(Todos)
admin.site.register(List)
