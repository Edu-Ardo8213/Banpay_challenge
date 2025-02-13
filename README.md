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

local
📌 Swagger UI: http://127.0.0.1/swagger/
📌 Admin Django: http://127.0.0.1/admin/

produccion
📌 Swagger UI: http://3.21.21.6/swagger/
📌 Admin Django: http://3.21.21.6/admin/

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


📂 Estructura del Proyecto

Este proyecto sigue una estructura modular para facilitar la escalabilidad y mantenimiento.

📁 Directorios y Archivos Principales

🌍 Raíz del Proyecto

manage.py → Script principal de Django.

requirements.txt → Dependencias del proyecto.

Dockerfile → Configuración de Docker.

docker-compose.yml → Configuración de los contenedores.

entrypoint.sh → Script de inicio de la aplicación en Docker.

.env → Variables de entorno.

README.md → Documentación del proyecto.

⚙️ Configuración Global (config/)

config/settings.py → Configuración principal de Django.

config/urls.py → Definición de rutas principales del proyecto.

config/wsgi.py → Configuración WSGI para despliegue.

config/asgi.py → Configuración ASGI (opcional para WebSockets).

config/__init__.py → Archivo de inicialización del módulo.

🛠️ Aplicaciones (app/)

📌 Aplicación de Usuarios (users/)

users/migrations/ → Migraciones de base de datos.

users/admin.py → Configuración del panel de administración.

users/models.py → Modelos de la base de datos.

users/serializers.py → Serializadores para DRF.

users/views.py → Lógica de negocio y endpoints.

users/urls.py → Definición de rutas de la aplicación.

users/tests.py → Pruebas unitarias de la aplicación.

users/__init__.py → Archivo de inicialización del módulo.

🎨 Archivos Estáticos y Medios

staticfiles/ → Archivos estáticos (colocados con collectstatic).

mediafiles/ → Archivos subidos por los usuarios.

🏗️ Entorno Virtual (Opcional)

venv/ → Entorno virtual de Python (si no usas Docker).

📌 Esta estructura permite una organización clara y facilita el mantenimiento del proyecto. 🚀




📝 Notas Adicionales

Si hay errores con archivos estáticos, ejecutar:

docker-compose exec web python manage.py collectstatic --noinput

Para reiniciar los contenedores completamente:

docker-compose down -v && docker-compose up --build -d

📜 Licencia

MIT License © 2025 - Tu Eduardo Daniel Cortés Moreno 

