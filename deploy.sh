#!/bin/bash
python manage.py makemigrations url
docker build -t zilioti.dev/shortner .
docker-compose up -d