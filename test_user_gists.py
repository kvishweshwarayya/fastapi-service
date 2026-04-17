from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_gists():
    response = client.get("/octocat")
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert data["user"] == "octocat"
    assert isinstance(data["gists"], list)
