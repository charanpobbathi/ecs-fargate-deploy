import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Check if the home page returns 200 OK"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_data(client):
    """Check if the home page returns the correct JSON message"""
    response = client.get('/')
    data = response.get_json()
    assert data['message'] == "Hello from ECS Fargate!"

def test_health_endpoint(client):
    """Check if the health endpoint returns healthy status"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"