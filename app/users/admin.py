from django.contrib import admin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "role")  # Solo mostrar estos campos en el admin
    list_filter = ("role",)  # Filtrar por rol en el admin
    search_fields = ("username",)  # Habilitar búsqueda por username
    ordering = ("username",)  # Ordenar por username


admin.site.register(User, CustomUserAdmin)
