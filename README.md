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

createdb django_todos   # for postgres

update models to match meteor
add ddp.py file and set up Collections and Publictions

python manage.py makemigrations

python manage.py migrate

export PYTHONPATH="${PYTHONPATH}:~/<path to your-django-project base_dir>/djme_todos"

DJANGO_SETTINGS_MODULE=djme_todos.settings dddp

DDP_DEFAULT_CONNECTION_URL=http://localhost:8000/ meteor


queries = [
      models.List.objects.filter(userId=''),
  ]
