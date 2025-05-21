#!/usr/bin/env bash

sudo chown -R $USER:$USER .

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Migrating database"
python manage.py migrate --noinput

echo "Starting server"
python -m gunicorn --bind 0.0.0.0:8000 --workers 4 blog.wsgi:application
