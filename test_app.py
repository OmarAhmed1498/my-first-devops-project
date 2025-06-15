from app import app

def test_hello():
    client = app.test_client()  # Create a test client for the Flask app
    response = client.get('/')  # Simulate a GET request to the homepage
    assert response.status_code == 200  # Check if the response is OK
    assert b'Hello, World! This is my DevOps project.' in response.data  # Check the response content