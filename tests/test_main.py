from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """
    Test the root endpoint to ensure it returns a successful status code
    and contains the expected HTML content, reflecting the UI change.
    """
    response = client.get("/")
    
    # 1. Assert the status code is still 200 (Success)
    assert response.status_code == 200
    
    # 2. Assert the Content-Type is text/html
    assert response.headers['content-type'].startswith('text/html')
    
    # 3. Assert the response text contains the expected greeting
    # This verifies the animated UI is present.
    assert "Hello, DevSecOps!" in response.text
    
    # 4. Assert the response text contains the link to API Docs
    assert 'Check API Docs: <a href="/docs"' in response.text
