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

def test_create_courier():
    response = client.post("/couriers", json={"name": "John Doe", "districts": ["District 1", "District 2"]})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["districts"] == ["District 1", "District 2"]