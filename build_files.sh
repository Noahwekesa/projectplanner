#!/bin/bash

# Install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Migrations and migrate
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collectstatic
python3 manage.py collectstatic --noinput
