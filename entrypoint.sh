#!/bin/sh

echo "Ejecutando Flake8 para linteo de código..."
flake8 || echo "⚠️ Se encontraron problemas de linteo"

echo "Aplicando Black para formatear código..."
black . || echo "⚠️ Se encontraron problemas en el formateo"

echo "Aplicando makemigrations..."
python manage.py makemigrations

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Verificando si el superusuario ya existe..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("Superusuario creado correctamente.")
else:
    print("El superusuario ya existe.")
EOF

echo "Iniciando servidor..."
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
