import pytest
import requests
from rest_framework.test import APIClient
from rest_framework import status
from app.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    return User.objects.create(username="testuser", role="admin")

@pytest.fixture
def access_token(test_user):
    refresh = RefreshToken.for_user(test_user)
    return str(refresh.access_token)

@pytest.fixture
def admin_user(db):
    return User.objects.create(username="adminuser", role="admin")

@pytest.fixture
def admin_access_token(admin_user):
    refresh = RefreshToken.for_user(admin_user)
    return str(refresh.access_token)



# ================== TESTS PARA USUARIOS ==================

def test_create_user(api_client, db):
    payload = {"username": "newuser", "role": "people"}
    response = api_client.post("/api/users/create/", payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["username"] == "newuser"

def test_get_users(api_client, test_user, access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = api_client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

def test_get_user(api_client, test_user, access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = api_client.get(f"/api/users/{test_user.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == test_user.username

def test_update_user(api_client, test_user, access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    payload = {"role": "films"}
    response = api_client.put(f"/api/users/{test_user.id}/update/", payload, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["role"] == "films"

def test_delete_user(api_client, test_user, access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = api_client.delete(f"/api/users/{test_user.id}/delete/")
    assert response.status_code == status.HTTP_204_NO_CONTENT


# ================== TESTS PARA AUTENTICACIÓN ==================

def test_obtain_token(api_client, test_user):
    payload = {"username": test_user.username}
    response = api_client.post("/api/token/", payload, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data

def test_refresh_token(api_client, access_token):
    refresh = RefreshToken.for_user(User.objects.get(username="testuser"))
    payload = {"refresh": str(refresh)}
    response = api_client.post("/api/token/refresh/", payload, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data

