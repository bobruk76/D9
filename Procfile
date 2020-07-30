release: python manage.py migrate --fake-initial
release: python manage.py loaddata fixtures.json
web: gunicorn todoapp.wsgi
