#!/bin/bash

# install requirements
python -m pip install -r requirements.txt

python manage.py collectstatic --noinput
