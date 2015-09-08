meteor create --example todos

virtualenv env

source ./env/bin/activate

pip install django
pip install django-ddp

django-admin.py startproject djme_todos

cd djme_todos

django-admin.py startapp django_todos

INSTALLED_APPS = (
    'django.contrib.admin',
    ............
    'dddp',
    'dddp.accounts',
    'django_todos',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_todos',
    }
}

createdb django_todos

python manage.py migrate

export PYTHONPATH="${PYTHONPATH}:~/<path to django root>/djme_todos"

DJANGO_SETTINGS_MODULE=djme_todos.settings dddp
