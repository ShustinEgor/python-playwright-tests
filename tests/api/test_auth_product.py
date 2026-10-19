import pytest
from src.api.http_client import api_get
from src.api.schemas.product import ProductDetail
from src.api.schemas.errors import ErrorBodyResponse
from src.api.test_data.product_payloads import PRODUCT_IDS, PRODUCT_WITHOUT_TOKEN

@pytest.mark.parametrize("product_id, expected_status", PRODUCT_IDS)
def test_get_product_with_token(auth_token, product_id, expected_status):
    response = api_get(f"/auth/products/{product_id}", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == expected_status
    body = response.json()

    if expected_status == 404:
        error = ErrorBodyResponse(**body)
        assert error.message == f"Product with id '{product_id}' not found"
    elif expected_status == 200:
        product = ProductDetail(**body)
        assert product.id == product_id
    else:
        pytest.fail(f"такой '{response.status_code}' еще не обрабатывался")

@pytest.mark.parametrize("product_id, expected_status", PRODUCT_WITHOUT_TOKEN)
def test_get_product_without_token(product_id, expected_status):
    response = api_get(f"/auth/products/{product_id}")
    assert response.status_code == expected_status
    body = response.json()
    error = ErrorBodyResponse(**body)
    assert error.message == "Access Token is required"


