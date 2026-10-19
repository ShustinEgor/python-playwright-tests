import requests
import logging
from src.config import BASE_URL

logger = logging.getLogger(__name__)

def _request(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{BASE_URL}{path}"
    logger.info(f"{method} {url}")
    response = requests.request(method, url, **kwargs)
    logger.info(f"Ответ: {response.status_code} от {response.url}")
    return response

def api_post(path, **kwargs):
    return _request("POST", path, **kwargs)

def api_get(path, **kwargs):
    return _request("GET", path, **kwargs)

def api_delete(path, **kwargs):
    return _request("DELETE", path, **kwargs)

def api_patch(path, **kwargs):
    return _request("PATCH", path, **kwargs)

def api_put(path, **kwargs):
    return _request("PUT", path, **kwargs)