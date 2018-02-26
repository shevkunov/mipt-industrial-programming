#!/bin/bash

echo "Sleeping for the connection..."
sleep 17

python manage.py migrate
python manage.py makemigrations list
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
