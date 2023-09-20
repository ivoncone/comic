#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=settings
python manage.py migrate --settings=settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=settings config.wsgi:application --bind 0.0.0.0:$PORT