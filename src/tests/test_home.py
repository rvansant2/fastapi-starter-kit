# tests/test_home.py
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.home.router import router as home_router

# Instantiate FastAPI app
app = FastAPI()
# Add and include home router
app.include_router(home_router)

# Instantiate FastAPI TestClient
client = TestClient(app)

def test_home_endpoint():
    # Get response from endpoint
    response = client.get("/")
    # Check status code
    assert response.status_code == 200

    # Get JSON data
    json_data = response.json()
    # Check structure
    assert "data" in json_data
    data = json_data["data"]

    # Check keys in data structure
    assert "name" in data
    assert "description" in data
    assert "version" in data
