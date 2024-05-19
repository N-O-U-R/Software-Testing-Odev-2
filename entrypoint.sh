#!/bin/bash

python manage.py makemigrations
# Apply migrations
python manage.py migrate
# Create a staff user
python manage.py create_staff_user

# Start the Django server
python manage.py runserver 0.0.0.0:3000
