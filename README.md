🚀 API de Banpay Challange con Django, PostgreSQL y Docker

Este proyecto es una API REST para la gestión de usuarios con autenticación JWT y permisos según roles. Los usuarios pueden consultar datos desde la API de Studio Ghibli según su rol.

📌 Características

✅ API REST con Django Rest Framework (DRF)
✅ Autenticación con JWT usando djangorestframework-simplejwt
✅ Base de datos PostgreSQL
✅ Contenedores Docker con docker-compose
✅ Documentación automática con Swagger
✅ Manejo de archivos estáticos con collectstatic
✅ Integración con la API de Studio Ghibli

🛠️ Tecnologías Utilizadas

Django (Backend)

Django Rest Framework (DRF) (API REST)

PostgreSQL (Base de Datos)

Docker & Docker Compose (Contenedores)

Gunicorn (Servidor de Aplicación)

drf-yasg (Swagger para documentación de API)

Flake8 & Black (Linteo de código)

🚀 Instalación y Configuración

1️⃣ Clonar el Repositorio

git clone https://github.com/Edu-Ardo8213/Banpay_challenge
cd tu_repositorio

2️⃣ Crear el Archivo .env

Crea un archivo .env en la raíz del proyecto y agrega:

# Configuración de PostgreSQL
POSTGRES_DB=djangodb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

# API de Ghibli
API_GHIBLIAPI=https://ghibliapi.vercel.app/

3️⃣ Construir y Levantar los Contenedores

docker-compose up --build -d

4️⃣ Acceder a la Aplicación

📌 Swagger UI: http://127.0.0.1:8000/swagger/
📌 Admin Django: http://127.0.0.1:8000/admin/

📜 Endpoints Disponibles

🔐 Autenticación

POST /api/token/ → Obtener Token JWT

POST /api/token/refresh/ → Refrescar Token

👤 Gestión de Usuarios

GET /api/users/ → Obtener todos los usuarios

POST /api/users/create/ → Crear usuario

GET /api/users/{username}/ → Obtener un usuario específico

PUT /api/users/{username}/update/ → Actualizar usuario

DELETE /api/users/{username}/delete/ → Eliminar usuario

🎥 API de Ghibli (según rol del usuario)

GET /api/ghibli-data/{username}/ → Obtener datos de la API de Ghibli según el rol del usuario

🛠️ Testing

Para ejecutar los tests, usa:

docker-compose exec web pytest

🧹 Linteo de Código

1️⃣ Ejecutar Linteo Manualmente

Para verificar el código con Flake8:

docker-compose exec web flake8

Para formatear el código con Black:

docker-compose exec web black .

🏗️ Estructura del Proyecto

/proyecto-raiz
│── manage.py                # Script principal de Django
│── requirements.txt         # Dependencias del proyecto
│── Dockerfile               # Configuración de Docker
│── docker-compose.yml       # Configuración de los contenedores
│── entrypoint.sh            # Script de inicio de la aplicación en Docker
│── .env                     # Variables de entorno
│── README.md                # Documentación del proyecto
│
├── /config                  # Configuración global de Django
│   ├── __init__.py          # Inicialización del módulo
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # Rutas principales del proyecto
│   ├── wsgi.py              # Configuración WSGI para despliegue
│   ├── asgi.py              # Configuración ASGI (opcional)
│   └── __pycache__/         # Caché de Python (ignorar)
│
├── /app                     # Carpeta con las aplicaciones Django
│   ├── /users               # Aplicación Django "users"
│   │   ├── migrations/      # Migraciones de base de datos
│   │   ├── admin.py         # Configuración del admin de Django
│   │   ├── models.py        # Modelos de la base de datos
│   │   ├── serializers.py   # Serializadores de DRF
│   │   ├── views.py         # Vistas de Django
│   │   ├── urls.py          # Rutas de la aplicación
│   │   ├── tests.py         # Pruebas de la aplicación
│   │   └── __init__.py      # Archivo de inicialización del módulo
│
├── /staticfiles             # Archivos estáticos (colectados con `collectstatic`)
├── /mediafiles              # Archivos subidos por usuarios
└── /venv                    # Entorno virtual de Python (si no usas Docker)


📝 Notas Adicionales

Si hay errores con archivos estáticos, ejecutar:

docker-compose exec web python manage.py collectstatic --noinput

Para reiniciar los contenedores completamente:

docker-compose down -v && docker-compose up --build -d

📜 Licencia

MIT License © 2025 - Tu Eduardo Daniel Cortés Moreno 

