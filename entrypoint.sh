#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=api.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=api.settings
python manage.py migrate --settings=api.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=api.settings api.wsgi:application --bind 0.0.0.0:$PORT
