import pytest         
from src.api.http_client import api_post  
import logging

logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def start_end_logger(request):
    logger.info(f"Запуск теста: {request.node.name}")
    yield
    logger.info(f"Конец теста: {request.node.name}")

@pytest.fixture(scope="session")
def auth_token():
    payload = {"username": "emilys", "password": "emilyspass"}
    response = api_post("/auth/login", json=payload)
    yield response.json()["accessToken"]