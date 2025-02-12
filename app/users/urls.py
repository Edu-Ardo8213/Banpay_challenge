from django.urls import path
from .views import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
    obtain_token,
    refresh_token,
    get_ghibli_data,
)

urlpatterns = [
    path("users/", get_users, name="get_users"),
    path("users/create/", create_user, name="create_user"),
    path("users/<int:user_id>/", get_user, name="get_user"),
    path("users/<int:user_id>/update/", update_user, name="update_user"),
    path("users/<int:user_id>/delete/", delete_user, name="delete_user"),
    path("token/", obtain_token, name="obtain_token"),
    path("token/refresh/", refresh_token, name="refresh_token"),
    path("ghibli-data/<str:username>/", get_ghibli_data, name="get_ghibli_data"),
]
