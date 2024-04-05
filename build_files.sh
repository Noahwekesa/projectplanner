#!/bin/bash

# install requirements
python3 -m pip install -r requirements.txt

# migrations and migrate
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# collectstatic
python3 manage.py collectstatic --noinput
