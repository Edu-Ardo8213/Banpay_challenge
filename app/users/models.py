from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("films", "Films"),
        ("people", "People"),
        ("locations", "Locations"),
        ("species", "Species"),
        ("vehicles", "Vehicles"),
    ]
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        """Propiedad requerida para la autenticación en DRF."""
        return True  # Siempre devuelve `True` porque no tenemos autenticación de contraseña
