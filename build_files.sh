#!/bin/bash

# Upgrade pip
python3 -m pip install --upgrade pip

# Install requirements
python3 -m pip install -r requirements.txt

# Install tailwind
python3 manage.py tailwind install

# Collect static files
python3 manage.py collectstatic --noinput
