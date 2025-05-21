#!/bin/bash

# Define path to manage.py
MANAGE_PY="/app/manage.py"

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to start..."
sleep 1
echo "PostgreSQL is up and running."

# Apply migrations
echo "Applying database migrations"
python $MANAGE_PY migrate --noinput

# Collect static files
echo "Collecting static files"
python $MANAGE_PY collectstatic --noinput

# Rebuild Elasticsearch index
echo "Rebuilding search index"
yes | python $MANAGE_PY search_index --rebuild

sleep 1

# Start Gunicorn server
echo "Starting Gunicorn server..."
exec gunicorn blog.wsgi:application --bind 0.0.0.0:8000 --workers 4
