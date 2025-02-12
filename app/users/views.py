from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User
from .serializers import UserSerializer
import requests
import os


# Crear un nuevo usuario
@swagger_auto_schema(
    method="post",
    request_body=UserSerializer,
    responses={201: "Usuario creado correctamente"},
)
@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    """
    Crea un nuevo usuario en la base de datos.
    """
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Obtener todos los usuarios
@swagger_auto_schema(method="get", responses={200: UserSerializer(many=True)})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_users(request):
    """
    Retorna la lista de todos los usuarios registrados.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# Obtener un usuario específico
@swagger_auto_schema(method="get", responses={200: UserSerializer()})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    """
    Retorna los datos de un usuario específico.
    """
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# Actualizar un usuario existente
@swagger_auto_schema(
    method="put",
    request_body=UserSerializer,
    responses={200: "Usuario actualizado correctamente"},
)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    """
    Actualiza la información de un usuario existente.
    """
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eliminar un usuario
@swagger_auto_schema(
    method="delete", responses={204: "Usuario eliminado correctamente"}
)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    """
    Elimina un usuario de la base de datos.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response(
        {"message": "Usuario eliminado correctamente"},
        status=status.HTTP_204_NO_CONTENT,
    )


# Obtener un token JWT para autenticación
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=["username"],
    ),
    responses={200: "Token generado correctamente"},
)
@api_view(["POST"])
@permission_classes([AllowAny])
def obtain_token(request):
    """
    Genera un token de acceso JWT para autenticación.
    """
    username = request.data.get("username")
    user = User.objects.filter(username=username).first()

    if not user:
        return Response(
            {"detail": "Usuario no encontrado", "code": "user_not_found"}, status=404
        )

    refresh = RefreshToken.for_user(user)
    refresh["user_id"] = user.id  # ✅ Agregar el ID del usuario al token

    return Response({"refresh": str(refresh), "access": str(refresh.access_token)})


# Refrescar un token JWT
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "refresh": openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=["refresh"],
    ),
    responses={200: "Token refrescado correctamente"},
)
@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Genera un nuevo token de acceso a partir de un token de refresco.
    """
    refresh_token = request.data.get("refresh")
    try:
        refresh = RefreshToken(refresh_token)
        return Response({"access": str(refresh.access_token)})
    except Exception:
        return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "username",
            openapi.IN_PATH,
            description="Nombre de usuario",
            type=openapi.TYPE_STRING,
        )
    ],
    responses={
        200: "Datos obtenidos correctamente",
        404: "Usuario no existente",
        400: "Error en la solicitud",
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ghibli_data(request, username):
    """
    Obtiene datos de la API de Studio Ghibli basándose en el rol del usuario.
    Si el usuario no existe, devuelve un error.
    """
    user = User.objects.filter(username=username).first()

    if not user:
        return Response(
            {"detail": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND
        )

    base_url = os.getenv("API_GHIBLIAPI")

    if user.role == "admin":
        # Si el usuario es admin, obtener datos de todos los roles
        roles = [role[0] for role in User.ROLE_CHOICES if role[0] != "admin"]
        responses = {}

        for role in roles:
            url = f"{base_url}{role}"
            response = requests.get(url)

            if response.status_code == 200:
                responses[role] = response.json()
            else:
                responses[role] = {"error": f"No se pudo obtener datos de {role}"}

        return Response(responses, status=status.HTTP_200_OK)

    else:
        # Si el usuario tiene otro rol, hacer una petición a su respectiva categoría
        url = f"{base_url}{user.role}"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)

        return Response(
            {"error": "No se pudo obtener datos"}, status=status.HTTP_400_BAD_REQUEST
        )
