import pytest

from src.api.http_client import api_post, api_get
from src.api.schemas.auth import Auth
from src.api.schemas.errors import ErrorBodyResponse
from src.api.test_data.auth_payloads import CREDS_PAYLOADS

def test_auth_me(auth_token):
    response = api_get("/auth/me", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"

@pytest.mark.parametrize("payload, expected_status", CREDS_PAYLOADS, ids=["valid", "invalid_name", "invalid_pass", "empty"])
def test_auth(payload, expected_status):
    response = api_post("/auth/login", json=payload)

    assert response.status_code == expected_status
    body = response.json()

    if payload["username"] == "invalidName" or payload["password"] == "invalidpass":
        error = ErrorBodyResponse(**body)
        assert error.message == "Invalid credentials" 
    elif payload["username"] == "emilys" and payload["password"] == "emilyspass":
        auth = Auth(**body)
        assert auth.username == payload["username"]
    elif payload["username"] == "" and payload["password"] == "":
        error = ErrorBodyResponse(**body)
        assert error.message == "Username and password required" 
    else: 
        error = ErrorBodyResponse(**body)
        pytest.fail(f"обнаружен незафиксированный сценарий со статусом {expected_status} и c сообщением {error.message}")