from dddp.api import API, APIMixin, Collection, Publication, api_endpoint
from dddp.models import get_meteor_id, get_object, get_object_id
import models

# from django.contrib.auth.models import User


class List(Collection):
    model = models.List

    @api_endpoint('insert')
    def insert(self, params):
      obj = models.List(name=params['name'], incompleteCount=params['incompleteCount'])
      obj.save()
      obj.listId = get_meteor_id(obj)
      obj.save()

    @api_endpoint('update')
    def update(self, params, _set, other):
        obj = models.List.objects.get(pk=get_object_id(models.List, params['_id']))
        if '$set' in _set:
            for key, val in _set['$set'].items():
                setattr(obj, key, val)
                obj.save()
        if '$inc' in _set:
            for key, val in _set['$inc'].items():
                cur = getattr(obj, key)
                new_val = cur + val
                setattr(obj, key, new_val)
                obj.save()


class Todos(Collection):
    model = models.Todos

    @api_endpoint('insert')
    def insert(self, params):
        obj = models.Todos(
            listId = params['listId'],
            text=params['text'],
        )
        obj.save()

    @api_endpoint('update')
    def update(self, params, _set, other):
        obj = models.Todos.objects.get(pk=get_object_id(models.Todos, params['_id']))
        if '$set' in _set:
            for key, val in _set['$set'].items():
                setattr(obj, key, val)
                obj.save()


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
