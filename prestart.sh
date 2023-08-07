#!/usr/bin/bash

sleep 5;
python manage.py migrate

sleep 5;
python manage.py loaddata mydata.json

sleep 5;
python manage.py runserver 0.0.0.0:8000