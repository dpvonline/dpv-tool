#!/bin/sh

set -o errexit
set -o nounset

echo "Apply database migrations"
python manage.py migrate
echo "Apply test user"
python manage.py add_users
echo "Load main data"
python manage.py loaddata data/main/*.json
echo "Load test data"
python manage.py loaddata data/test/*.json

echo "Start server"
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
