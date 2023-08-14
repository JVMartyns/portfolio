python manage.py migrate
python manage.py seeds
python manage.py collectstatic --noinput --clear -v2
python manage.py runserver 0.0.0.0:8000