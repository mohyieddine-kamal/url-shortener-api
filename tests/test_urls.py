from fastapi.testclient import TestClient
import os
from main import app
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")



client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_short_url():
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com/articles/2026/10/python-fastapi-tutorial-complete-guide?ref=newsletter&utm_source=email"},
        headers={"x-api-key": API_KEY},
    )
    assert response.status_code == 201
    data = response.json()
    assert "short_code" in data
    assert data["click_count"] == 0


def test_create_short_url_without_api_key():
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com/articles/sans-cle-api"},
    )
    assert response.status_code == 422

def test_redirect_to_original():
    create_response = client.post(
        "/shorten",
        json={"original_url": "https://example.com/articles/page-a-rediriger"},
        headers={"x-api-key": API_KEY},
    )
    short_code = create_response.json()["short_code"]

    redirect_response = client.get(f"/{short_code}", follow_redirects=False)

    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"] == "https://example.com/articles/page-a-rediriger"


def test_redirect_code_not_found():
    response = client.get("/code-qui-nexiste-pas")
    assert response.status_code == 404

def test_create_short_url_with_wrong_api_key():
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com/articles/mauvaise-cle"},
        headers={"x-api-key": "cle_invalide"},
    )
    assert response.status_code == 401