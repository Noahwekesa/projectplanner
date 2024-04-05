#!/bin/bash

# install requirements
python3 -m pip install -r requirements.txt

# collectstatic
python3 manage.py collectstatic --noinput
