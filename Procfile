release: python manage.py migrate
release: python manage.py loaddata app.json
# web: gunicorn todoapp.wsgi


web: python manage.py runserver 0.0.0.0:$PORT