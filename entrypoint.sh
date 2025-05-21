#!/usr/bin/env bash

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Migrating database"
python manage.py migrate --noinput

echo "Starting server"
exec gunicorn blog.wsgi:application --bind 0.0.0.0:8000 --workers 4
