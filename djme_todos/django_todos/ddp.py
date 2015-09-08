from dddp.api import API, APIMixin, Collection, Publication, api_endpoint
from dddp.models import get_meteor_id, get_object, get_object_id
import models

# from django.contrib.auth.models import User


class List(Collection):
    model = models.List

class Todos(Collection):
    model = models.Todos


class publicLists(Publication):

  def get_queries(self):
    return [
        models.List.objects.filter(userId=None),
    ]

class privateLists(Publication):

  def get_queries(self, userId):
    return [
        models.List.objects.filter(userId=userId),
    ]

class todos(Publication):

    def get_queries(self, listId):
        return [
            models.Todos.objects.filter(listId=listId)
        ]



API.register([
    List,
    Todos,
    publicLists,
    privateLists,
    todos,
])
