from fastapi.testclient import TestClient
from main import app
from app.test2 import SessionLocal, get_db

client = TestClient(app)

def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_order():
    response = client.post("/orders", json={"name": "Order 1", "district": "District 1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Order 1"
    assert response.json()["district"] == "District 1"
    assert response.json()["status"] == 1