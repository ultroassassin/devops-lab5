import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_existed_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"

def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_create_user():
    new_user = {"id": 3, "name": "Charlie"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 200
    assert response.json() == new_user

def test_update_user():
    updated = {"id": 1, "name": "Alicia"}
    response = client.put("/users/1", json=updated)
    assert response.status_code == 200
    assert response.json()["name"] == "Alicia"

def test_delete_user():
    response = client.delete("/users/2")
    assert response.status_code == 200
    # Проверяем, что пользователя больше нет
    get_response = client.get("/users/2")
    assert get_response.status_code == 404
