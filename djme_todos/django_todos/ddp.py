from dddp.api import API, APIMixin, Collection, Publication, api_endpoint
from dddp.models import get_meteor_id, get_object, get_object_id
import models

# from django.contrib.auth.models import User


class List(Collection):
    model = models.List

    @api_endpoint('insert')
    def insert(self, params):
      print(params)
      obj = models.List(name=params['name'], incompleteCount=params['incompleteCount'])
      obj.save()

class Todos(Collection):
    model = models.Todos


class publicLists(Publication):

  queries = [
        models.List.objects.filter(userId=''),
    ]

class privateLists(Publication):

  queries = [
        models.List.objects.filter(userId=''),
    ]

class todos(Publication):

    def get_queries(self, listId):
        list_id = models.List.objects.get(pk=get_object_id(models.List, listId))
        print(list_id)
        print(models.Todos.objects.filter(listId=list_id))
        return [
            models.Todos.objects.filter(listId=list_id)
        ]



API.register([
    List,
    Todos,
    publicLists,
    privateLists,
    todos,
])
