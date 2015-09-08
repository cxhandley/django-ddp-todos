from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class List(models.Model):
    name = models.CharField(max_length=20)
    incompleteCount = models.IntegerField()
    userId = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Todos(models.Model):
    listId = models.ForeignKey('List')
    text = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.text
