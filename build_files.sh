#!/bin/bash

# install requirements
pip install -r requirements.txt
python manage.py collectstatic --noinput
