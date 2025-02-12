#!/bin/sh

echo "Aplicando makemigrations..."
python manage.py makemigrations

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Creando superusuario..."
python manage.py createsuperuser --noinput || true

echo "Iniciando servidor..."
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
