===========================
DJANGO METEOR TODOS EXAMPLE
===========================

This is an example app, providing a full working example of django integrating with meteor.

Installation
------------

The easiest way to get starting is to (assuming you have virtualenvwrapper):

    $ git clone https://github.com/django-ddp/django-ddp-todos.git
    $ cd django-ddp-todos
    $ mkvirtualenv ddp-todos
    $ workon ddp-todos
    * install postgresql if not installed
    $ createdb djme_todos
    * modify djme_todos/.env to set up DATABASE_URL
    $ pip install -r requirements.txt
    * install meteor https://www.meteor.com/install
    $ cd meteor/meteor_todos
    $ meteor build --directory ../build --server localhost:8000
    $ cd ../..
    $ add2virtualenv .
    $ python manage.py migrate
    $ DJANGO_SETTINGS_MODULE=djme_todos.settings dddp
    * go to http://localhost:8000


References
----------

  * DJANGO-DDP: https://github.com/django-ddp/django-ddp
  * METEOR TODOS: https://www.meteor.com/todos

License
-------------------

MIT License.
