===========================
DJANGO METEOR TODOS EXAMPLE
===========================

This is an example app, providing a full working example of django integrating with meteor.

Installation
------------

The easiest way to get starting is to (assuming you have virtualenvwrapper):

Clone the repo

.. code:: sh

    git clone https://github.com/django-ddp/django-ddp-todos.git
    cd django-ddp-todos

Make virtual environment (recommended)

.. code:: sh

    mkvirtualenv ddp-todos
    workon ddp-todos

Install postgresql if not installed

.. code:: sh

    createdb djme_todos

Copy djme_todos/.env_default to djme_todos/.env. Modify djme_todos/.env to your DATABASE_URL settings

Install requirements

.. code:: sh

    pip install -r requirements.txt

Install meteor https://www.meteor.com/install

Build the meteor app

.. code:: sh

    cd meteor/meteor_todos
    meteor build --directory ../build --server localhost:8000

Add directory to PYTHONPATH in virtualenv

.. code:: sh

    cd ../..
    add2virtualenv .

Run DJANGO

.. code:: sh

    python manage.py migrate
    DJANGO_SETTINGS_MODULE=djme_todos.settings dddp

Go to http://localhost:8000


References
----------

  * DJANGO-DDP: https://github.com/django-ddp/django-ddp
  * METEOR TODOS: https://www.meteor.com/todos

License
-------------------

MIT License.
