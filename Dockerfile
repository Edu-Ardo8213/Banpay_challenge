# Usar la imagen oficial de Python
FROM python:3.9

# Configurar variables de entorno
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Crear directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . /app/

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# Exponer el puerto donde correrá Django
EXPOSE 8000

# Comando para ejecutar Django en el contenedor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

CMD ["/entrypoint.sh"]