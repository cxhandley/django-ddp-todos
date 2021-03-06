from dddp.models import AleaIdMixin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class List(AleaIdMixin, models.Model):
    name = models.CharField(max_length=20)
    incompleteCount = models.IntegerField(default=0)
    user = models.ForeignKey('auth.User', null=True, blank=True)
    userId = models.CharField(max_length=20, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    meteor_collection = models.CharField(max_length=20, default='lists')

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Todos(AleaIdMixin, models.Model):
    listId = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    meteor_collection = models.CharField(max_length=20, default='todos')

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.text
