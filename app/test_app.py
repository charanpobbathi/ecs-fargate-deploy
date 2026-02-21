import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_html_content(client):
    """Verify that the H1 tag and the message exist in the HTML"""
    response = client.get('/')
    assert b"<h1>" in response.data
    assert b"Hello from ECS Fargate!" in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"

def test_logic_calculation():
    """Test a simple piece of logic independent of the web server."""
    result = 10 + 20
    assert result == 30