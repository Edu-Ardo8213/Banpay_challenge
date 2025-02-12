from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Obtiene el usuario a partir del token.
        """
        user_id = validated_token.get("user_id")  # JWT almacena el ID del usuario

        try:
            user = User.objects.get(id=user_id)  # Buscar en TU modelo de User
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found", code="user_not_found")

        return user
