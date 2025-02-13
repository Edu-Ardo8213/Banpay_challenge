# 🚀 API de Banpay Challenge con Django, PostgreSQL, Docker y AWS EC2

Este proyecto es una API REST para la gestión de usuarios con autenticación JWT y permisos según roles. Los usuarios pueden consultar datos desde la API de Studio Ghibli según su rol.

---

## 📌 Características

- ✅ API REST con Django Rest Framework (DRF)
- ✅ Autenticación con JWT usando `djangorestframework-simplejwt`
- ✅ Base de datos **PostgreSQL**
- ✅ Contenedores Docker con **docker-compose**
- ✅ Documentación automática con **Swagger**
- ✅ Manejo de archivos estáticos con `collectstatic`
- ✅ Integración con la API de **Studio Ghibli**
- ✅ **Despliegue en AWS EC2 con Nginx y Docker**

---

## 🛠️ Tecnologías Utilizadas

- **Django** (Backend)
- **Django Rest Framework (DRF)** (API REST)
- **PostgreSQL** (Base de Datos)
- **Docker & Docker Compose** (Contenedores)
- **Gunicorn** (Servidor de Aplicación)
- **Nginx** (Proxy inverso)
- **drf-yasg** (Swagger para documentación de API)
- **Flake8 & Black** (Linteo de código)

---

## 🚀 Instalación y Configuración

### ❶ Clonar el Repositorio
```bash
git clone https://github.com/Edu-Ardo8213/Banpay_challenge
cd Banpay_challenge
```

### ❷ Crear el Archivo `.env`
Crea un archivo `.env` en la raíz del proyecto y agrega:
```env
# Configuración de PostgreSQL
POSTGRES_DB=djangodb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

# API de Ghibli
API_GHIBLIAPI=https://ghibliapi.vercel.app/
```

### ❸ Construir y Levantar los Contenedores
```bash
docker-compose up --build -d
```

### ❹ Acceder a la Aplicación

#### **💻 Entorno Local:**
- 📀 **Swagger UI:** [http://127.0.0.1/swagger/](http://127.0.0.1/swagger/)
- 🏢 **Admin Django:** [http://127.0.0.1/admin/](http://127.0.0.1/admin/)

#### **🌐 Entorno de Producción en AWS EC2:**
- 📀 **Swagger UI:** [http://3.21.21.6/swagger/](http://3.21.21.6/swagger/)
- 🏢 **Admin Django:** [http://3.21.21.6/admin/](http://3.21.21.6/admin/)

---

## 📚 Endpoints Disponibles

### 🔒 Autenticación
- **POST** `/api/token/` ➔ Obtener Token JWT
- **POST** `/api/token/refresh/` ➔ Refrescar Token

### 👤 Gestión de Usuarios
- **GET** `/api/users/` ➔ Obtener todos los usuarios
- **POST** `/api/users/create/` ➔ Crear usuario
- **GET** `/api/users/{username}/` ➔ Obtener un usuario específico
- **PUT** `/api/users/{username}/update/` ➔ Actualizar usuario
- **DELETE** `/api/users/{username}/delete/` ➔ Eliminar usuario

### 🎥 API de Ghibli (según rol del usuario)
- **GET** `/api/ghibli-data/{username}/` ➔ Obtener datos de la API de Ghibli según el rol del usuario

---

## 🛠️ Testing
Ejecuta los tests con:
```bash
docker-compose exec web pytest
```

---

## 🤖 Linteo de Código

### ❶ Ejecutar Linteo Manualmente

Para verificar el código con **Flake8**:
```bash
docker-compose exec web flake8
```

Para formatear el código con **Black**:
```bash
docker-compose exec web black .
```

---

## 📂 Estructura del Proyecto

```plaintext
Banpay_challenge/
│── manage.py                     # Script principal de Django
│── requirements.txt               # Dependencias del proyecto
│── Dockerfile                     # Configuración de Docker
│── docker-compose.yml              # Configuración de los contenedores
│── entrypoint.sh                   # Script de inicio en Docker
│── .env                            # Variables de entorno
│── README.md                       # Documentación del proyecto
│
├── config/                         # Configuración global de Django
│   ├── settings.py                 # Configuración principal
│   ├── urls.py                     # Rutas principales
│   ├── wsgi.py                     # Configuración WSGI
│   ├── asgi.py                     # Configuración ASGI
│
├── app/                            # Aplicaciones Django
│   ├── users/                      # Aplicación de usuarios
│   │   ├── models.py               # Modelos de la BD
│   │   ├── serializers.py          # Serializadores
│   │   ├── views.py                # Lógica de negocio
│   │   ├── urls.py                 # Rutas de la app
│   │   ├── tests.py                # Pruebas
│   │
├── staticfiles/                    # Archivos estáticos (colocados con collectstatic)
├── mediafiles/                      # Archivos subidos por usuarios
├── venv/                            # Entorno virtual de Python (si no usas Docker)
```

---

## 📘 Notas Adicionales

Si hay errores con archivos estáticos, ejecuta:
```bash
docker-compose exec web python manage.py collectstatic --noinput
```

Para reiniciar los contenedores completamente:
```bash
docker-compose down -v && docker-compose up --build -d
```

---

## 📝 Licencia
MIT License © 2025 - Eduardo Daniel Cortés Moreno

