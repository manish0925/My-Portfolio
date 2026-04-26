#!/usr/bin/env bash

pip install -r requirements.txt

# FORCE CREATE MIGRATIONS
python manage.py makemigrations core

# APPLY MIGRATIONS
python manage.py migrate

# COLLECT STATIC
python manage.py collectstatic --noinput
