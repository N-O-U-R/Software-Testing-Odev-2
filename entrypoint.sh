#!/bin/bash

# Exit script on error
set -e

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Optionally create a staff user
python manage.py create_staff_user

# Start Django server in the background
python manage.py runserver 0.0.0.0:3000
