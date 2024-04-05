#!/bin/bash

# Create a virtual environment
python3 -m virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install tailwind (if necessary, adjust this line according to your project requirements)
python manage.py tailwind install

# Collect static files
python manage.py collectstatic --noinput
