#!/bin/bash

# install requirements
python3 -m pip install -r requirements.txt
pyython3 -m python manage.py tailwind install

# collectstatic
python3 manage.py collectstatic --noinput
